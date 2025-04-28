Subject: Master Plan Checklist: RDL Generation Tool Development

**Directive Section:**

*   **Context:** Develop a PowerShell module tool (`RdlGenerator`) capable of generating SSRS RDL files programmatically from a JSON configuration file (`report_definition.json`). The initial target is to replicate the structure and content of `Comprehensive Table Comparison (1).rdl`.
*   **Execution Mode:** Fully autonomous execution by SE-Apex agent.
*   **Mandatory Standards:** Adherence to the **Apex Software Compliance Standards Guide v1.5** (located at `docs/STANDARDS.md`) is **MANDATORY** for all Phases, Tasks, Steps, and deliverables. Specific rules referenced as `(Rule #N: CODE)` MUST be complied with. The Standards Guide takes precedence unless deviations are explicitly noted and justified herein.
*   **Sequential Execution:** Execution MUST follow the hierarchical Phase -> Task -> Step structure sequentially. Checkboxes (`- [ ]`) MUST be marked complete (`- [x]`) only after the item is fully finished and internally verified according to its `Internal Success Criteria` and `Internal Verification Method`. Do NOT proceed until the current item is verified complete.
*   **Reporting Constraints:** Intermediate reporting is DISABLED. Progress is tracked internally via checkbox state and the internal test log. Final reporting occurs ONLY upon completion of the entire sequence.
*   **Internal Logging:** Log test results and verification outcomes internally per the `Test Reporting Protocol`.

**Test Reporting Protocol (Internal):**

*   **Log File:** `docs/rdl_generator_test_log.md`
*   **Format:** Markdown table per test execution.
*   **Data Points:** | Date | Scope (Function/Task) | Test Type (Unit/Integration) | Result (Pass/Fail) | Coverage % (If applicable) | Findings/Notes | Rule Compliance Verified |
*   **Update Frequency:** Update after each `Task Completion Testing` or `Phase Completion Testing` block.

---

- [ ] **Phase 1: Foundation & Configuration**
    *   **Objective:** Define the input configuration structure and create an initial configuration file based on the existing target RDL.
    *   ---
    *   - [x] **Task 1.1: Define Configuration Schema**
        *   - [x] * **Step 1.1.1 (Rule #10: DES-ARCH-DEFINE):** Analyze the structure, elements, attributes, and namespaces of the target RDL file (`Comprehensive Table Comparison (1).rdl`) to identify all required components for configuration (DataSources, DataSets, Parameters, ReportItems like Textbox/Tablix, Layout, Styling).
        *   - [x] * **Step 1.1.2 (Rule #11: DES-DETAIL-IMPL):** Design the JSON schema structure (`report_definition_schema.json`) to represent the identified RDL components logically and comprehensively. Include definitions for properties, types, nesting, and required fields. Define options like 'auto' for field detection.
        *   - [x] * **Step 1.1.3 (Rule #56: DOC-API):** Document the JSON schema, explaining the purpose of each section and property. Save as `docs/report_definition_schema_guide.md`.
        *   **Internal Success Criteria:**
            *   JSON schema (`report_definition_schema.json`) exists and is well-formed.
            *   Schema accurately covers all essential elements identified in Step 1.1.1 (DataSources, Parameters, Datasets, Fields, ReportItems - Textbox/Tablix, Layout, basic Style properties).
            *   Schema documentation (`docs/report_definition_schema_guide.md`) exists and clearly explains the schema structure.
            *   Compliance with referenced Apex Standards Rules (10, 11, 56).
        *   **Internal Verification Method:**
            *   Review `report_definition_schema.json` against the analysis from Step 1.1.1.
            *   Validate `report_definition_schema.json` using a JSON Schema validator tool/library.
            *   Review `docs/report_definition_schema_guide.md` for clarity and completeness.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Log verification results (Schema validation pass/fail, documentation review) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [x] **Task 1.2: Create Initial Configuration File**
        *   - [x] * **Step 1.2.1:** Read the content of the existing RDL file (`Comprehensive Table Comparison (1).rdl`).
        *   - [x] * **Step 1.2.2 (Rule #60: IMPL-REQ):** Manually translate the structure and content of the RDL file into a JSON file (`report_definition.json`) strictly adhering to the schema defined in Task 1.1.
        *   - [x] * **Step 1.2.3:** Save the resulting JSON configuration to `report_definition.json` in the project root.
        *   **Internal Success Criteria:**
            *   `report_definition.json` file exists in the project root.
            *   The file contains valid JSON content.
            *   The JSON content successfully validates against `report_definition_schema.json`.
            *   The content accurately represents the structure and key values of the original `Comprehensive Table Comparison (1).rdl`.
            *   Compliance with referenced Apex Standards Rules (60).
        *   **Internal Verification Method:**
            *   Check file existence (`report_definition.json`).
            *   Validate the file content using a JSON validator.
            *   Validate the file content against the `report_definition_schema.json` using a schema validator.
            *   Manually compare key sections (e.g., dataset names, parameter names, main report items) between `report_definition.json` and `Comprehensive Table Comparison (1).rdl`.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Log verification results (JSON validation, Schema validation, manual comparison outcome) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   **Phase Completion Testing (Internal):** N/A for Phase 1.

---

- [x] **Phase 1: Foundation & Configuration**
    *   **Objective:** Define the input configuration structure and create an initial configuration file based on the existing target RDL.
    *   ---
    *   - [x] **Task 1.1: Define Configuration Schema**
        *   - [x] * **Step 1.1.1 (Rule #10: DES-ARCH-DEFINE):** Analyze the structure, elements, attributes, and namespaces of the target RDL file (`Comprehensive Table Comparison (1).rdl`) to identify all required components for configuration (DataSources, DataSets, Parameters, ReportItems like Textbox/Tablix, Layout, Styling).
        *   - [x] * **Step 1.1.2 (Rule #11: DES-DETAIL-IMPL):** Design the JSON schema structure (`report_definition_schema.json`) to represent the identified RDL components logically and comprehensively. Include definitions for properties, types, nesting, and required fields. Define options like 'auto' for field detection.
        *   - [x] * **Step 1.1.3 (Rule #56: DOC-API):** Document the JSON schema, explaining the purpose of each section and property. Save as `docs/report_definition_schema_guide.md`.
        *   **Internal Success Criteria:**
            *   JSON schema (`report_definition_schema.json`) exists and is well-formed.
            *   Schema accurately covers all essential elements identified in Step 1.1.1 (DataSources, Parameters, Datasets, Fields, ReportItems - Textbox/Tablix, Layout, basic Style properties).
            *   Schema documentation (`docs/report_definition_schema_guide.md`) exists and clearly explains the schema structure.
            *   Compliance with referenced Apex Standards Rules (10, 11, 56).
        *   **Internal Verification Method:**
            *   Review `report_definition_schema.json` against the analysis from Step 1.1.1.
            *   Validate `report_definition_schema.json` using a JSON Schema validator tool/library.
            *   Review `docs/report_definition_schema_guide.md` for clarity and completeness.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Log verification results (Schema validation pass/fail, documentation review) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [x] **Task 1.2: Create Initial Configuration File**
        *   - [x] * **Step 1.2.1:** Read the content of the existing RDL file (`Comprehensive Table Comparison (1).rdl`).
        *   - [x] * **Step 1.2.2 (Rule #60: IMPL-REQ):** Manually translate the structure and content of the RDL file into a JSON file (`report_definition.json`) strictly adhering to the schema defined in Task 1.1.
        *   - [x] * **Step 1.2.3:** Save the resulting JSON configuration to `report_definition.json` in the project root.
        *   **Internal Success Criteria:**
            *   `report_definition.json` file exists in the project root.
            *   The file contains valid JSON content.
            *   The JSON content successfully validates against `report_definition_schema.json`.
            *   The content accurately represents the structure and key values of the original `Comprehensive Table Comparison (1).rdl`.
            *   Compliance with referenced Apex Standards Rules (60).
        *   **Internal Verification Method:**
            *   Check file existence (`report_definition.json`).
            *   Validate the file content using a JSON validator.
            *   Validate the file content against the `report_definition_schema.json` using a schema validator.
            *   Manually compare key sections (e.g., dataset names, parameter names, main report items) between `report_definition.json` and `Comprehensive Table Comparison (1).rdl`.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Log verification results (JSON validation, Schema validation, manual comparison outcome) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   **Phase Completion Testing (Internal):** N/A for Phase 1.

---

- [ ] **Phase 2: Core Generation Logic (PowerShell Module)**
    *   **Objective:** Implement the core PowerShell module functions for parsing the configuration and generating the data-related sections of the RDL (DataSources, Parameters, Datasets).
    *   ---
    *   - [ ] **Task 2.1: Setup PowerShell Module Structure**
        *   - [ ] * **Step 2.1.1:** Create a new directory named `RdlGenerator` in the project root.
        *   - [ ] * **Step 2.1.2 (Rule #12: DES-MODULARITY):** Create empty files `RdlGenerator.psm1` (module script) and `RdlGenerator.psd1` (module manifest) inside the `RdlGenerator` directory.
        *   - [ ] * **Step 2.1.3:** Add basic manifest content to `RdlGenerator.psd1` (e.g., RootModule, ModuleVersion).
        *   **Internal Success Criteria:**
            *   `RdlGenerator` directory exists.
            *   `RdlGenerator.psm1` and `RdlGenerator.psd1` files exist within the directory.
            *   `RdlGenerator.psd1` contains basic valid manifest structure.
            *   Compliance with referenced Apex Standards Rules (12).
        *   **Internal Verification Method:**
            *   Check file system for the directory and files.
            *   Read `RdlGenerator.psd1` and verify basic manifest structure.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Log verification results (File/Dir existence check, Manifest check) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [ ] **Task 2.2: Implement Configuration Parser**
        *   - [ ] * **Step 2.2.1 (Rule #11: DES-DETAIL-IMPL):** Define a PowerShell function `Parse-ReportConfiguration` within `RdlGenerator.psm1` that accepts a file path parameter (`-ConfigurationPath`). Export the function in the manifest (`.psd1`).
        *   - [ ] * **Step 2.2.2 (Rule #60: IMPL-REQ):** Implement the function logic to read the file content from the specified path.
        *   - [ ] * **Step 2.2.3 (Rule #60: IMPL-REQ, Rule #23: DATA-CHECKALL):** Use `ConvertFrom-Json` to parse the file content. Validate that essential top-level properties (e.g., `reportName`, `dataSets`, `reportLayout`) exist in the resulting object.
        *   - [ ] * **Step 2.2.4 (Rule #61: ERR-HDL):** Add error handling (e.g., using `try/catch`) for file not found, invalid JSON format, and missing essential properties. Throw terminating errors on failure.
        *   - [ ] * **Step 2.2.5:** Return the parsed PowerShell object on success.
        *   **Internal Success Criteria:**
            *   Function `Parse-ReportConfiguration` is defined in `.psm1` and exported in `.psd1`.
            *   Function successfully reads and parses a valid `report_definition.json` file.
            *   Function returns a PowerShell object matching the JSON structure.
            *   Function throws appropriate errors for non-existent file, invalid JSON, or missing key properties.
            *   Compliance with referenced Apex Standards Rules (11, 60, 23, 61).
        *   **Internal Verification Method:**
            *   Code review of the function implementation and manifest export.
            *   Create and execute unit tests (using Pester framework) for `Parse-ReportConfiguration`:
                *   Test case with valid `report_definition.json`.
                *   Test case with path to non-existent file.
                *   Test case with an invalid JSON file.
                *   Test case with a JSON file missing a required top-level property.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run Pester unit tests for `Parse-ReportConfiguration`. Log results (Pass/Fail for each case) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [ ] **Task 2.3: Implement Data Source & Parameter Generation**
        *   - [ ] * **Step 2.3.1 (Rule #11: DES-DETAIL-IMPL):** Define internal (not exported) helper functions `New-RdlDataSourceXml` and `New-RdlReportParameterXml` within `RdlGenerator.psm1`. These functions should accept relevant configuration objects (derived from the output of `Parse-ReportConfiguration`) and return `System.Xml.XmlElement` objects.
        *   - [ ] * **Step 2.3.2 (Rule #60: IMPL-REQ):** Implement `New-RdlDataSourceXml` to create the `<DataSource>` XML element with its `Name` attribute and `<DataSourceReference>` child element based on the configuration. Use `.NET System.Xml` types (e.g., `XmlDocument.CreateElement`). Ensure correct RDL namespace (`http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition`).
        *   - [ ] * **Step 2.3.3 (Rule #60: IMPL-REQ):** Implement `New-RdlReportParameterXml` to create the `<ReportParameter>` XML element with its `Name` attribute and child elements (`DataType`, `Prompt`, `AllowBlank`, `MultiValue`, `DefaultValue`, `ValidValues` with `DataSetReference`) based on the configuration object for a single parameter. Handle optional elements correctly. Ensure correct RDL namespace.
        *   **Internal Success Criteria:**
            *   Functions `New-RdlDataSourceXml` and `New-RdlReportParameterXml` are defined.
            *   Functions accept appropriate PowerShell configuration objects.
            *   Functions return valid `System.Xml.XmlElement` objects representing the corresponding RDL fragments with correct structure, attributes, child elements, and namespace based on sample input data.
            *   Compliance with referenced Apex Standards Rules (11, 60).
        *   **Internal Verification Method:**
            *   Code review of function implementations.
            *   Create and execute Pester unit tests for each function:
                *   Provide sample configuration data (e.g., a hashtable representing a data source or a parameter).
                *   Call the function and validate the properties (`Name`, `NamespaceURI`, child nodes, attributes) of the returned `XmlElement` object against expected values.
                *   Test handling of optional elements (e.g., `DefaultValue`, `ValidValues`).
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run Pester unit tests for `New-RdlDataSourceXml` and `New-RdlReportParameterXml`. Log results in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [ ] **Task 2.4: Implement Dataset Generation (incl. Auto-Detect)**
        *   - [ ] * **Step 2.4.1 (Rule #11: DES-DETAIL-IMPL):** Define internal helper function `New-RdlDataSetXml` within `RdlGenerator.psm1`. It should accept a dataset configuration object and potentially DB connection parameters (if auto-detect is used). It should return an `XmlElement`.
        *   - [ ] * **Step 2.4.2 (Rule #60: IMPL-REQ):** Implement the main `<DataSet>` element creation with `Name` attribute and child `<Query>` element (containing `DataSourceName`, `CommandType`, `CommandText`, and `<QueryParameters>` generated using logic similar to Task 2.3).
        *   - [ ] * **Step 2.4.3 (Rule #60: IMPL-REQ):** Implement the `<Fields>` element generation. If the `fields` property in the config is an array, iterate through it and create `<Field>` elements with `Name` attribute and `DataField`/`TypeName` children. Use the 'rd' namespace (`http://schemas.microsoft.com/SQLServer/reporting/reportdesigner`) for `TypeName`.
        *   - [ ] * **Step 2.4.4 (Rule #60: IMPL-REQ, Rule #27: SEC-KEY-STORAGE, Rule #61: ERR-HDL):** Implement the 'auto-detect' logic. If `fields` is 'auto':
            *   Define parameters for DB connection info (Server, Database, Credentials). Consider how these will be passed securely (e.g., function parameters, environment variables - DO NOT hardcode (Rule #25: CONF-HARD)).
            *   Use `System.Data.SqlClient` to connect to the database.
            *   Execute `sys.sp_describe_first_result_set` with the `CommandText` from the config. Handle potential parameters needed by the SP (this might require refinement - assume parameterless SPs for initial implementation or require parameters in config).
            *   Parse the result set to get column names (`name`) and map SQL types to RDL `TypeName` values (e.g., `varchar` -> `System.String`, `int` -> `System.Int32`).
            *   Generate `<Field>` elements based on the query results.
            *   Implement robust error handling for connection failures, query errors, and type mapping issues. Ensure connections are closed properly (`finally` block).
        *   **Internal Success Criteria:**
            *   Function `New-RdlDataSetXml` is defined.
            *   Function generates a valid `<DataSet>` XML element including `<Query>` and `<QueryParameters>`.
            *   Function correctly generates `<Fields>` based on a static list in the configuration.
            *   Function correctly generates `<Fields>` using 'auto-detect' by querying the database (requires test setup).
            *   Secure handling of DB credentials is considered (no hardcoding).
            *   Error handling for DB operations is implemented.
            *   Compliance with referenced Apex Standards Rules (11, 60, 27, 61, 25).
        *   **Internal Verification Method:**
            *   Code review, focusing on XML generation, static field handling, auto-detect logic, credential handling, and error handling.
            *   Pester unit tests:
                *   Test with a dataset config using a static field list. Validate output XML.
                *   Test with a dataset config using 'auto'. This requires an integration test setup:
                    *   A test SQL Server database with a sample stored procedure.
                    *   Mechanism to provide connection details securely to the test.
                    *   Execute the function and validate the generated `<Fields>` against the known output of the test SP.
                *   Test error handling scenarios (invalid connection string, SP not found, etc.).
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run Pester unit and integration tests for `New-RdlDataSetXml`. Log results in `docs/rdl_generator_test_log.md`.
    *   ---
    *   **Phase Completion Testing (Internal):** Manually review the created functions in `RdlGenerator.psm1`. Ensure all unit/integration tests for Phase 2 Tasks passed. Update `docs/rdl_generator_test_log.md` with overall Phase 2 status.

---

- [ ] **Phase 3: Visual Element Generation**
    *   **Objective:** Implement functions to generate the XML for visual report items (Textbox, Tablix) and handle styling.
    *   ---
    *   - [ ] **Task 3.1: Implement Textbox Generation**
        *   - [ ] * **Step 3.1.1 (Rule #11: DES-DETAIL-IMPL):** Define internal helper function `New-RdlTextboxXml` within `RdlGenerator.psm1`, accepting a textbox configuration object and returning an `XmlElement`.
        *   - [ ] * **Step 3.1.2 (Rule #60: IMPL-REQ):** Implement generation of the `<Textbox>` element with its `Name` attribute.
        *   - [ ] * **Step 3.1.3 (Rule #60: IMPL-REQ):** Generate child elements like `<CanGrow>`, `<KeepTogether>`, and the `<Paragraphs><Paragraph><TextRuns><TextRun><Value>` structure based on the configuration's `value` property (which might be a literal string or an expression like `=Fields!FieldName.Value`).
        *   - [ ] * **Step 3.1.4 (Rule #60: IMPL-REQ):** Generate basic positioning/sizing properties (Top, Left, Height, Width) directly on the `<Textbox>` element.
        *   - [ ] * **Step 3.1.5:** Implement a placeholder call to a (yet to be created) styling function `Add-RdlStyleXml` to add a basic `<Style>` node.
        *   **Internal Success Criteria:**
            *   Function `New-RdlTextboxXml` is defined.
            *   Function generates a valid `<Textbox>` XML fragment including Name, Value structure, and position/size attributes based on sample config.
            *   Compliance with referenced Apex Standards Rules (11, 60).
        *   **Internal Verification Method:**
            *   Code review.
            *   Pester unit tests with sample textbox configurations (literal value, expression value). Validate the output `XmlElement` structure and attributes.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run Pester unit tests for `New-RdlTextboxXml`. Log results in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [ ] **Task 3.2: Implement Tablix Generation**
        *   *Task Objective:* Implement the generation of the complex Tablix structure. This will be iterative, starting with the basics.
        *   - [ ] * **Step 3.2.1 (Rule #11: DES-DETAIL-IMPL):** Define internal helper function `New-RdlTablixXml` within `RdlGenerator.psm1`, accepting a Tablix configuration object and returning an `XmlElement`.
        *   - [ ] * **Step 3.2.2 (Rule #60: IMPL-REQ):** Generate the main `<Tablix>` element with `Name` attribute and `DataSetName` child element. Add position/size attributes.
        *   - [ ] * **Step 3.2.3 (Rule #60: IMPL-REQ):** Generate the `<TablixBody>` element. Inside it, generate `<TablixColumns>` containing a `<TablixColumn>` with `<Width>` for each column defined in the configuration.
        *   - [ ] * **Step 3.2.4 (Rule #60: IMPL-REQ):** Generate the `<TablixRows>` element.
            *   Generate the first `<TablixRow>` for the header. Set its `<Height>`. Inside `<TablixCells>`, generate a `<TablixCell>` containing a `<Textbox>` (using `New-RdlTextboxXml`) for each column header defined in the config. Apply basic header styling (e.g., BackgroundColor).
            *   Generate the second `<TablixRow>` for the detail row. Set its `<Height>`. Inside `<TablixCells>`, generate a `<TablixCell>` containing a `<Textbox>` (using `New-RdlTextboxXml`) bound to the corresponding field (`=Fields!FieldName.Value`) for each column defined in the config.
        *   - [ ] * **Step 3.2.5 (Rule #60: IMPL-REQ):** Generate the `<TablixColumnHierarchy>` containing a `<TablixMembers>` node with one `<TablixMember/>` for each column.
        *   - [ ] * **Step 3.2.6 (Rule #60: IMPL-REQ):** Generate the `<TablixRowHierarchy>` containing `<TablixMembers>` with:
            *   A `<TablixMember>` for the header row (with `<KeepWithGroup>After</KeepWithGroup>`).
            *   A `<TablixMember>` for the detail row (containing `<Group Name="Details"><DataElementName>Detail</DataElementName></Group>` and `<TablixMembers><TablixMember/></TablixMembers>`).
        *   - [ ] * **Step 3.2.7:** Add a basic `<Style>` node to the main `<Tablix>` element (e.g., border).
        *   **Internal Success Criteria:**
            *   Function `New-RdlTablixXml` is defined.
            *   Function generates a valid XML fragment representing a basic Tablix structure (Body, Columns, Header Row, Detail Row, basic Hierarchies) based on sample configuration.
            *   Textbox elements for headers and details are correctly generated and bound.
            *   Compliance with referenced Apex Standards Rules (11, 60).
        *   **Internal Verification Method:**
            *   Code review of the complex generation logic.
            *   Pester unit tests with a sample Tablix configuration. Validate the output `XmlElement` structure against a known-good basic Tablix XML fragment. Check column counts, row counts, header text, detail bindings.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run Pester unit tests for `New-RdlTablixXml`. Log results in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [ ] **Task 3.3: Implement Styling Engine**
        *   - [ ] * **Step 3.3.1 (Rule #11: DES-DETAIL-IMPL, Rule #12: DES-MODULARITY):** Define an internal helper function `Add-RdlStyleXml` that accepts a parent `XmlElement` and a style configuration object (hashtable). Alternatively, enhance `New-RdlTextboxXml` and `New-RdlTablixXml` to handle style objects directly.
        *   - [ ] * **Step 3.3.2 (Rule #60: IMPL-REQ):** Implement logic within the chosen function(s) to parse the style configuration object (properties like `fontFamily`, `fontSize`, `fontWeight`, `color`, `backgroundColor`, `borderStyle`, `borderWidth`, `borderColor`, `paddingLeft`, `paddingRight`, `paddingTop`, `paddingBottom`, `textAlign`, `verticalAlign`, `format`).
        *   - [ ] * **Step 3.3.3 (Rule #60: IMPL-REQ):** Create or find the `<Style>` child element on the parent XML element.
        *   - [ ] * **Step 3.3.4 (Rule #60: IMPL-REQ):** Generate the appropriate child XML elements within `<Style>` (e.g., `<FontFamily>`, `<FontSize>`, `<BackgroundColor>`, `<Border><Style/></Border>`, `<PaddingLeft>`) based on the properties present in the style configuration object. Handle units for sizes (e.g., `pt`, `in`).
        *   - [ ] * **Step 3.3.5:** Integrate calls to the styling logic within `New-RdlTextboxXml` and `New-RdlTablixXml` (for cell/header styling).
        *   **Internal Success Criteria:**
            *   Styling logic exists (either dedicated function or integrated).
            *   Logic correctly parses style configuration objects.
            *   Correct `<Style>` XML structure and child elements are generated based on the configuration.
            *   Styling is applied to Textbox and Tablix elements as configured.
            *   Compliance with referenced Apex Standards Rules (11, 12, 60).
        *   **Internal Verification Method:**
            *   Code review of styling logic.
            *   Pester unit tests:
                *   Test the styling function/logic with various style configurations (different properties, units). Validate the generated `<Style>` XML fragment.
                *   Modify unit tests for `New-RdlTextboxXml` and `New-RdlTablixXml` to include style configurations and verify the `<Style>` node is correctly added/populated.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run Pester unit tests for styling logic. Log results in `docs/rdl_generator_test_log.md`.
    *   ---
    *   **Phase Completion Testing (Internal):** Manually review the created visual element generation functions. Ensure all unit tests for Phase 3 Tasks passed. Update `docs/rdl_generator_test_log.md` with overall Phase 3 status.

---

- [ ] **Phase 4: Assembly & Testing**
    *   **Objective:** Assemble the generated XML fragments into a complete RDL file and perform final validation.
    *   ---
    *   - [ ] **Task 4.1: Implement RDL Assembly Function**
        *   - [ ] * **Step 4.1.1 (Rule #11: DES-DETAIL-IMPL):** Define the main exported function `New-RdlReport` in `RdlGenerator.psm1`. It should accept the `-ConfigurationPath` parameter and an optional `-OutputPath` parameter.
        *   - [ ] * **Step 4.1.2 (Rule #60: IMPL-REQ):** Call `Parse-ReportConfiguration` to load the config.
        *   - [ ] * **Step 4.1.3 (Rule #60: IMPL-REQ):** Create a new `System.Xml.XmlDocument`. Create the root `<Report>` element with required namespaces (xmlns, xmlns:rd, xmlns:df, xmlns:am).
        *   - [ ] * **Step 4.1.4 (Rule #60: IMPL-REQ):** Generate and append `<DataSources>`, `<DataSets>`, `<ReportParameters>`, `<ReportParametersLayout>`, `<Body><ReportItems>`, `<Page>` sections in the correct order.
            *   Iterate through config sections, call the corresponding `New-Rdl...Xml` helper functions (DataSource, Parameter, DataSet, Textbox, Tablix), and append the returned `XmlElement` objects (imported using `ImportNode`) to the appropriate parent node in the main document.
        *   - [ ] * **Step 4.1.5 (Rule #60: IMPL-REQ):** Add other required top-level elements like `<AutoRefresh>`, `<df:DefaultFontFamily>`, `<rd:ReportUnitType>`, etc.
        *   - [ ] * **Step 4.1.6 (Rule #60: IMPL-REQ, Rule #61: ERR-HDL):** Save the completed `XmlDocument` to the specified `-OutputPath` (or a default path based on `reportName`). Implement error handling for file saving.
        *   **Internal Success Criteria:**
            *   Function `New-RdlReport` is defined and exported.
            *   Function orchestrates calls to parser and generator functions correctly.
            *   Function assembles a complete and structurally valid RDL XML document.
            *   Function saves the document to a file.
            *   Basic error handling for file operations is present.
            *   Compliance with referenced Apex Standards Rules (11, 60, 61).
        *   **Internal Verification Method:**
            *   Code review of the assembly logic and orchestration.
            *   Integration test:
                *   Provide the path to the `report_definition.json` created in Phase 1.
                *   Execute `New-RdlReport`.
                *   Verify that an output RDL file is created.
                *   Validate the output RDL file against the official RDL XSD schema (requires obtaining the XSD).
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Run integration test for `New-RdlReport`. Log results (File creation, XSD validation result) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   - [ ] **Task 4.2: Final Validation and Refinement**
        *   - [ ] * **Step 4.2.1 (Rule #32: TEST-PLAN-PROC):** Use an XML diff tool to compare the generated RDL file (from Task 4.1 integration test) against the original `Comprehensive Table Comparison (1).rdl`. Document significant differences.
        *   - [ ] * **Step 4.2.2 (Rule #33: TEST-REQ-COVERAGE):** Open the generated RDL file in SSRS Report Builder or Visual Studio with the SSDT extension.
        *   - [ ] * **Step 4.2.3 (Rule #33: TEST-REQ-COVERAGE):** Verify that the report preview renders without errors. Check layout, basic styling, and data binding for the main tables and textboxes.
        *   - [ ] * **Step 4.2.4 (Rule #42: SA-DEFECT-MGMT):** Identify any rendering errors, layout issues, styling discrepancies, or functional differences compared to the original report or the configuration intent.
        *   - [ ] * **Step 4.2.5 (Rule #42: SA-DEFECT-MGMT):** Debug the PowerShell module code (`RdlGenerator.psm1`) or adjust the `report_definition.json` configuration to fix identified issues. Re-run `New-RdlReport` and repeat verification steps (4.2.1-4.2.4) until the output is satisfactory.
        *   - [ ] * **Step 4.2.6 (Rule #62: FINAL-SWEEP):** Perform a final sweep of the PowerShell code and configuration file, checking for compliance with relevant Apex Standards (e.g., no hardcoded values (Rule #25: CONF-HARD), placeholders (Rule #59: IMPL-PLACE), consistent formatting (Rule #17: QUAL-FMT)).
        *   - [ ] * **Step 4.2.7 (Rule #58: DOC-EXT):** Create/update a README.md file explaining how to use the `RdlGenerator` module and the `report_definition.json` format.
        *   **Internal Success Criteria:**
            *   Generated RDL is functionally and visually equivalent to the original RDL (or accurately reflects the `report_definition.json` specification).
            *   Generated RDL renders correctly without errors in SSRS tools.
            *   No outstanding high-priority defects remain.
            *   Code and configuration pass the `FINAL-SWEEP` checks.
            *   Usage documentation (README.md) exists.
            *   Compliance with referenced Apex Standards Rules (32, 33, 42, 62, 25, 59, 17, 58).
        *   **Internal Verification Method:**
            *   Review XML diff results.
            *   Confirm successful rendering and visual correctness in SSRS tools.
            *   Review defect log/fix history.
            *   Execute `FINAL-SWEEP` checklist against code and config.
            *   Review README.md for completeness and clarity.
            *   Verify compliance with all referenced Apex Standards Rules for this Task and its Steps.
        *   **Task Completion Testing (Internal):** Log final validation results (Diff summary, SSRS rendering status, Final Sweep pass/fail, README review) in `docs/rdl_generator_test_log.md`.
    *   ---
    *   **Phase Completion Testing (Internal):** Ensure all Phase 4 tests passed and the final generated RDL meets requirements. Update `docs/rdl_generator_test_log.md` with overall Phase 4 status.

---

**Final Instruction:**

Begin execution of Phase 1, Task 1. Proceed sequentially through all Phases, Tasks, and Steps as defined. Mark each item as complete (`- [x]`) only after successful internal verification. Adhere strictly to the **Apex Software Compliance Standards Guide v1.5** (`docs/STANDARDS.md`) throughout execution. Log all test results internally to `docs/rdl_generator_test_log.md`. Report ONLY upon successful completion of all phases or if an unrecoverable error occurs.

*(Instructions based on requirements established as of 2025-04-08 18:08. Location context: c:/Users/jlietz/Desktop/Projects/SQL Projects/comprehensive_table_comparison)*
