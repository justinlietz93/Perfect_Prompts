// Prompt template and builder for Rust.
// Usage:
//     use prompt::{CODEX_PROMPT, build_prompt};
//     let s = build_prompt("September 30, 2025", "VDM Physics Checklist");
//     println!("{}", s);

pub const CODEX_PROMPT: &str = r#"Today's date is {todays_date}:
Review and comprehensively and meticulously update the {checklist_name} and when that’s done, begin working through each item one step at a time.  

For each step you take, reason about 5 possible high quality options / solutions. Then organize the options based on relevance and likelihood of success based on current context. Choose the top one, then critique your choice. Begin working if you still agree with decision, taking extra long to think and reason through each step. 

Be very critical of your own reasoning and correct yourself as needed. Once you've completed the step, review your work again from the perspective of a strict judge.


Respect these tasks, as they require superior quality over speed / quantity. Only the most qualified and capable agents are assigned to this work.

Check off your items and document your work in the checklist as you go.

Mark items as [STARTED] [RETRYING - {one word reason}] [DONE] [NOT STARTED]

MAKE SURE TO TEST ALL OPERATIONS FROM MULTIPLE ANGLES, ESPECIALLY AGENTIC OPERATIONS.

Work your way through testing methodically from atomic unit tests up to manual system flow tests.

When you finish and are ready to provide your update response, briefly mention how things are going and what your next plans are.
"#;

pub fn build_prompt(todays_date: &str, checklist_name: &str) -> String {
    CODEX_PROMPT
        .replace("{todays_date}", todays_date)
        .replace("{checklist_name}", checklist_name)
}
