pub fn chunk_summary_prompt_metrics_dashboard(text: &str) -> String {
    format!(r#"
You are an expert data analyst AI. Your task is to analyze the following document segment and extract all Key Performance Indicators (KPIs) and their associated metric values.

Follow these instructions:
1.  Identify all measurable indicators (e.g., uptime, latency, revenue, error rate, active users).
2.  For each KPI, extract any of the following values if mentioned:
    *   **Current:** The most recent measurement.
    *   **Min / Max:** The observed lower and upper bounds.
    *   **Average / Median:** An aggregate baseline value.
    *   **Target / Threshold:** A benchmark or goal value.
    *   **Status:** An explicit status like "on-track", "at-risk", "off-track", or symbols (✔, ⚠, ✖).
3.  Also, identify the **Timeframe** for these metrics if mentioned (e.g., "Last 30 days", "Q2 2025").
4.  Format the extracted information as a clear Markdown list. If no specific timeframe is mentioned in this segment, state it.
5.  If no KPIs or metrics are found in this segment, state "No metrics were identified in this segment."

**EXAMPLE FORMAT:**
*   **Timeframe:** Last 30 Days
*   **KPI: API Uptime (%)**
    *   Current: 99.7
    *   Min: 98.9
    *   Max: 100
    *   Average: 99.5
    *   Target: 99.9
    *   Status: ⚠
*   **KPI: Response Latency (ms)**
    *   Current: 210
    *   Target: <=250
    *   Status: ✔

---
DOCUMENT SEGMENT TO ANALYZE:
{}
---

Provide the extracted metrics for the segment above.
"#, text)
}

pub fn reduce_summaries_prompt_metrics_dashboard(text: &str) -> String {
    format!(r#"
You are an expert data synthesizer and report generator. You have been given a series of notes extracted from a larger document, each detailing various Key Performance Indicators (KPIs) and their metrics.
Your task is to synthesize all these notes into a single, comprehensive Metrics Dashboard table in Markdown format.

Follow these instructions:
1.  Identify a single, overarching **Timeframe** for the report. If different timeframes are mentioned, select the most frequently cited one or the most recent one.
2.  Identify all unique **KPIs** from the notes. Each unique KPI should be a row in your table.
3.  Construct a Markdown table with the following columns: \`KPI\`, \`Current\`, \`Min\`, \`Max\`, \`Avg\`, \`Target\`, and \`Status\`.
4.  Fill in the cells of the table with the corresponding values for each KPI.
5.  If a value for a specific cell is not mentioned in the notes (e.g., 'Min' is missing for a KPI), use "N/A" for that cell.
6.  For the 'Status' column, use symbols (✔, ⚠, ✖) if they can be inferred from the text or are explicitly stated. Otherwise, use "N/A".
7.  The final output must be a clean, well-formatted, and easy-to-read Markdown table. It should be preceded by a title indicating the timeframe, like "### Service Monitoring Dashboard (Last 30 Days)". Do not include any other text before or after the title and table.

---
NOTES TO SYNTHESIZE:
{}
---

Provide the single, synthesized Metrics Dashboard Markdown table below.
"#, text)
}
