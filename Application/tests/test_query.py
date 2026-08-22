from perfect_prompts.infrastructure.search.query import parse_search_query


def test_beacon_query_semantics_are_preserved():
    parsed = parse_search_query('find "session handoff" prompt templates')
    assert parsed.fts_expression == '("session handoff") AND ("prompt"* OR "templates"*)'
