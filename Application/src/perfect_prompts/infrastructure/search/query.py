from __future__ import annotations

import re
from collections import deque
from dataclasses import dataclass
from typing import Iterable

WORD_PATTERN = re.compile(r"[\w]+", flags=re.UNICODE)
QUOTED_PHRASE_PATTERN = re.compile(r'"([^"]*)"')
STOP_WORDS = {
    "a", "about", "all", "an", "and", "are", "as", "at", "be", "been",
    "but", "by", "can", "did", "do", "does", "file", "files", "find",
    "for", "from", "had", "has", "have", "how", "i", "in", "into", "is",
    "it", "me", "most", "of", "on", "or", "our", "project", "related",
    "show", "that", "the", "their", "there", "these", "this", "to", "was",
    "were", "what", "when", "where", "which", "who", "why", "with",
}


@dataclass(frozen=True, slots=True)
class QuotedPhrase:
    raw: str
    tokens: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ParsedSearchQuery:
    raw: str
    terms: tuple[str, ...]
    quoted_phrases: tuple[QuotedPhrase, ...]

    @property
    def match_mode(self) -> str:
        if self.quoted_phrases and self.terms:
            return "mixed"
        if self.quoted_phrases:
            return "quoted_phrase"
        if self.terms:
            return "broad_terms"
        return "empty"

    @property
    def fts_expression(self) -> str:
        phrases = [f'"{" ".join(phrase.tokens)}"' for phrase in self.quoted_phrases]
        terms = [f'"{term}"*' for term in self.terms]
        phrase_expression = " AND ".join(phrases)
        term_expression = " OR ".join(terms)
        if phrase_expression and term_expression:
            return f"({phrase_expression}) AND ({term_expression})"
        return phrase_expression or term_expression


def query_terms(query: str) -> list[str]:
    raw = WORD_PATTERN.findall(query.casefold())
    terms: list[str] = []
    seen: set[str] = set()
    for term in raw:
        if len(term) < 2 or term in STOP_WORDS or term in seen:
            continue
        seen.add(term)
        terms.append(term)
    return terms[:24]


def parse_search_query(query: str) -> ParsedSearchQuery:
    if query.count('"') % 2:
        raise ValueError("A quoted phrase is missing its closing double quote.")
    phrases: list[QuotedPhrase] = []
    seen_phrases: set[tuple[str, ...]] = set()
    unquoted_parts: list[str] = []
    cursor = 0
    for match in QUOTED_PHRASE_PATTERN.finditer(query):
        unquoted_parts.append(query[cursor:match.start()])
        tokens = normalized_word_tokens(match.group(1))
        if tokens and tokens not in seen_phrases:
            seen_phrases.add(tokens)
            phrases.append(QuotedPhrase(match.group(1), tokens))
        cursor = match.end()
    unquoted_parts.append(query[cursor:])
    return ParsedSearchQuery(query, tuple(query_terms(" ".join(unquoted_parts))), tuple(phrases))


def normalized_word_tokens(text: str) -> tuple[str, ...]:
    return tuple(match.group(0).casefold() for match in WORD_PATTERN.finditer(text))


def fields_match_all_phrases(phrases: Iterable[QuotedPhrase], *fields: str | None) -> bool:
    searchable_fields = tuple(field or "" for field in fields)
    return all(any(_contains_token_sequence(field, phrase.tokens) for field in searchable_fields) for phrase in phrases)


def _contains_token_sequence(text: str, phrase: tuple[str, ...]) -> bool:
    if not phrase:
        return True
    window: deque[str] = deque(maxlen=len(phrase))
    for match in WORD_PATTERN.finditer(text):
        window.append(match.group(0).casefold())
        if len(window) == len(phrase) and tuple(window) == phrase:
            return True
    return False
