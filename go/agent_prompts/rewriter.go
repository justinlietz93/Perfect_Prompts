package agent_prompts

import "fmt"

// RewriteLength represents the desired length of rewritten content
type RewriteLength string

const (
	RewriteLengthConcise RewriteLength = "concise"
	RewriteLengthShort   RewriteLength = "short"
	RewriteLengthMedium  RewriteLength = "medium"
	RewriteLengthLong    RewriteLength = "long"
)

// RewriterPromptTemplate generates a rewriter prompt with specified parameters
func RewriterPromptTemplate(style, instructions string, length RewriteLength) string {
	var lengthInstruction string
	
	switch length {
	case RewriteLengthConcise:
		lengthInstruction = "The final output should be concise, like a social media post or an email (approx. 100-200 words)."
	case RewriteLengthShort:
		lengthInstruction = "The final output should be short, like a short essay or a blog post (approx. 500-800 words)."
	case RewriteLengthMedium:
		lengthInstruction = "The final output should be a moderate length, like a blog post or a detailed article section (approx. 1000-1500 words)."
	case RewriteLengthLong:
		lengthInstruction = "The final output should be extensive and detailed, like a chapter of a book or a long-form report (approx. 2000-5000 words)."
	default:
		lengthInstruction = "The final output should be a moderate length, like a blog post or a detailed article section (approx. 1000-1500 words)."
	}

	instructionsText := instructions
	if instructionsText == "" {
		instructionsText = "None provided."
	}

	return fmt.Sprintf(`
You are an expert writer and content creator. Your task is to rewrite the provided content (which may include text and images) into a new narrative.
Follow the user-provided style and instructions precisely.

**STYLE GUIDE:**
---
%s
---

**ADDITIONAL INSTRUCTIONS:**
---
%s
---

**DESIRED LENGTH:**
---
%s
---

Now, analyze the following content pieces and rewrite them into a single, cohesive narrative according to the rules above.
If images are provided, describe them and weave their content into the story.
The output should be in well-formatted Markdown.
`, style, instructionsText, lengthInstruction)
}