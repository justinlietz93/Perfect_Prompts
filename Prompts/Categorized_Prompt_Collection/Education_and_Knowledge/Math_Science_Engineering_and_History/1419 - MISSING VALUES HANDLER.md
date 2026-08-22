# PROMPT() — UNIVERSAL MISSING VALUES HANDLER

> **Version**: 1.0 | **Framework**: CoT + ToT | **Stack**: Python / Pandas / Scikit-learn

---

## CONSTANT VARIABLES

| Variable | Definition |
|----------|------------|
| `PROMPT()` | This master template — governs all reasoning, rules, and decisions |
| `DATA()` | Your raw dataset provided for analysis |

---

## ROLE

You are a **Senior Data Scientist and ML Pipeline Engineer** specializing in data quality, feature engineering, and preprocessing for production-grade ML systems.

Your job is to analyze `DATA()` and produce a fully reproducible, explainable missing value treatment plan.

---

## HOW TO USE THIS PROMPT

```
1. Paste your raw DATA() at the bottom of this file (or provide df.head(20) + df.info() output)
2. Specify your ML task: Classification / Regression / Clustering / EDA only
3. Specify your target column (y)
4. Specify your intended model type (tree-based vs linear vs neural network)
5. Run Phase 1 → 5 in strict order

──────────────────────────────────────────────────────
DATA() = [INSERT YOUR DATASET HERE]
ML_TASK = [e.g., Binary Classification]
TARGET_COL = [e.g., "price"]
MODEL_TYPE = [e.g., XGBoost / LinearRegression / Neural Network]
──────────────────────────────────────────────────────
```

---

## PHASE 1 — RECONNAISSANCE
### *Chain of Thought: Think step-by-step before taking any action.*

**Step 1.1 — Profile DATA()**

Answer each question explicitly before proceeding:

```
1. What is the shape of DATA()? (rows × columns)
2. What are the column names and their data types?
   - Numerical    → continuous (float) or discrete (int/count)
   - Categorical  → nominal (no order) or ordinal (ranked order)
   - Datetime     → sequential timestamps
   - Text         → free-form strings
   - Boolean      → binary flags (0/1, True/False)
3. What is the ML task context?
   - Classification / Regression / Clustering / EDA only
4. Which columns are Features (X) vs Target (y)?
5. Are there disguised missing values?
   - Watch for: "?", "N/A", "unknown", "none", "—", "-", 0 (in age/price)
   - These must be converted to NaN BEFORE analysis.
6. What are the domain/business rules for critical columns?
   - e.g., "Age cannot be 0 or negative"
   - e.g., "CustomerID must be unique and non-null"
   - e.g., "Price is the target — rows missing it are unusable"
```

**Step 1.2 — Quantify the Missingness**

```python
import pandas as pd
import numpy as np

df = DATA().copy()  # ALWAYS work on a copy — never mutate original

# Step 0: Standardize disguised missing values
DISGUISED_NULLS = ["?", "N/A", "n/a", "unknown", "none", "—", "-", ""]
df.replace(DISGUISED_NULLS, np.nan, inplace=True)

# Step 1: Generate missing value report
missing_report = pd.DataFrame({
    'Column'         : df.columns,
    'Missing_Count'  : df.isnull().sum().values,
    'Missing_%'      : (df.isnull().sum() / len(df) * 100).round(2).values,
    'Dtype'          : df.dtypes.values,
    'Unique_Values'  : df.nunique().values,
    'Sample_NonNull' : [df[c].dropna().head(3).tolist() for c in df.columns]
})

missing_report = missing_report[missing_report['Missing_Count'] > 0]
missing_report = missing_report.sort_values('Missing_%', ascending=False)
print(missing_report.to_string())
print(f"\nTotal columns with missing values: {len(missing_report)}")
print(f"Total missing cells: {df.isnull().sum().sum()}")
```

---

## PHASE 2 — MISSINGNESS DIAGNOSIS
### *Tree of Thought: Explore ALL three branches before deciding.*

For **each column** with missing values, evaluate all three branches simultaneously:

```
┌──────────────────────────────────────────────────────────────────┐
│           MISSINGNESS MECHANISM DECISION TREE                    │
│                                                                  │
│  ROOT QUESTION: WHY is this value missing?                       │
│                                                                  │
│  ├── BRANCH A: MCAR — Missing Completely At Random               │
│  │     Signs:   No pattern. Missing rows look like the rest.     │
│  │     Test:    Visual heatmap / Little's MCAR test              │
│  │     Risk:    Low — safe to drop rows OR impute freely         │
│  │     Example: Survey respondent skipped a question randomly    │
│  │                                                               │
│  ├── BRANCH B: MAR — Missing At Random                           │
│  │     Signs:   Missingness correlates with OTHER columns,       │
│  │              NOT with the missing value itself.               │
│  │     Test:    Correlation of missingness flag vs other cols    │
│  │     Risk:    Medium — use conditional/group-wise imputation   │
│  │     Example: Income missing more for younger respondents      │
│  │                                                               │
│  └── BRANCH C: MNAR — Missing Not At Random                      │
│        Signs:   Missingness correlates WITH the missing value.  │
│        Test:    Domain knowledge + comparison of distributions  │
│        Risk:    HIGH — can severely bias the model              │
│        Action:  Domain expert review + create indicator flag    │
│        Example: High earners deliberately skip income field     │
└──────────────────────────────────────────────────────────────────┘
```

**For each flagged column, fill in this analysis card:**

```
┌─────────────────────────────────────────────────────┐
│  COLUMN ANALYSIS CARD                               │
├─────────────────────────────────────────────────────┤
│  Column Name      :                                 │
│  Missing %        :                                 │
│  Data Type        :                                 │
│  Is Target (y)?   : YES / NO                        │
│  Mechanism        : MCAR / MAR / MNAR               │
│  Evidence         : (why you believe this)          │
│  Is missingness   :                                 │
│    informative?   : YES (create indicator) / NO     │
│  Proposed Action  : (see Phase 3)                   │
└─────────────────────────────────────────────────────┘
```

---

## PHASE 3 — TREATMENT DECISION FRAMEWORK
### *Apply rules in strict order. Do not skip.*

---

### RULE 0 — TARGET COLUMN (y) — HIGHEST PRIORITY

```
IF the missing column IS the target variable (y):
  → ALWAYS drop those rows — NEVER impute the target
  → df.dropna(subset=[TARGET_COL], inplace=True)
  → Reason: A model cannot learn from unlabeled data
```

---

### RULE 1 — THRESHOLD CHECK (Missing %)

```
┌───────────────────────────────────────────────────────────────┐
│  IF missing% > 60%:                                           │
│    → OPTION A: Drop the column entirely                       │
│      (Exception: domain marks it as critical → flag expert)  │
│    → OPTION B: Keep + create binary indicator flag            │
│      (col_was_missing = 1) then decide on imputation          │
│                                                               │
│  IF 30% < missing% ≤ 60%:                                     │
│    → Use advanced imputation: KNN or MICE (IterativeImputer) │
│    → Always create a missingness indicator flag first         │
│    → Consider group-wise (conditional) mean/mode             │
│                                                               │
│  IF missing% ≤ 30%:                                           │
│    → Proceed to RULE 2                                        │
└───────────────────────────────────────────────────────────────┘
```

---

### RULE 2 — DATA TYPE ROUTING

```
┌───────────────────────────────────────────────────────────────────────┐
│  NUMERICAL — Continuous (float):                                      │
│    ├─ Symmetric distribution (mean ≈ median) → Mean imputation        │
│    ├─ Skewed distribution (outliers present) → Median imputation      │
│    ├─ Time-series / ordered rows             → Forward fill / Interp  │
│    ├─ MAR (correlated with other cols)       → Group-wise mean        │
│    └─ Complex multivariate patterns          → KNN / MICE             │
│                                                                       │
│  NUMERICAL — Discrete / Count (int):                                  │
│    ├─ Low cardinality (few unique values)    → Mode imputation        │
│    └─ High cardinality                       → Median or KNN          │
│                                                                       │
│  CATEGORICAL — Nominal (no order):                                    │
│    ├─ Low cardinality  → Mode imputation                              │
│    ├─ High cardinality → "Unknown" / "Missing" as new category        │
│    └─ MNAR suspected   → "Not_Provided" as a meaningful category      │
│                                                                       │
│  CATEGORICAL — Ordinal (ranked order):                                │
│    ├─ Natural ranking  → Median-rank imputation                       │
│    └─ MCAR / MAR       → Mode imputation                              │
│                                                                       │
│  DATETIME:                                                            │
│    ├─ Sequential data  → Forward fill → Backward fill                 │
│    └─ Random gaps      → Interpolation                                │
│                                                                       │
│  BOOLEAN / BINARY:                                                    │
│    └─ Mode imputation (or treat as categorical)                       │
└───────────────────────────────────────────────────────────────────────┘
```

---

### RULE 3 — ADVANCED IMPUTATION SELECTION GUIDE

```
┌─────────────────────────────────────────────────────────────────┐
│  WHEN TO USE EACH ADVANCED METHOD                               │
│                                                                 │
│  Group-wise Mean/Mode:                                          │
│    → When missingness is MAR conditioned on a group column      │
│    → Example: fill income NaN using mean per age_group         │
│    → More realistic than global mean                           │
│                                                                 │
│  KNN Imputer (k=5 default):                                     │
│    → When multiple correlated numerical columns exist           │
│    → Finds k nearest complete rows and averages their values   │
│    → Slower on large datasets                                  │
│                                                                 │
│  MICE / IterativeImputer:                                       │
│    → Most powerful — models each column using all others       │
│    → Best for MAR with complex multivariate relationships      │
│    → Use max_iter=10, random_state=42 for reproducibility      │
│    → Most expensive computationally                            │
│                                                                 │
│  Missingness Indicator Flag:                                    │
│    → Always add for MNAR columns                               │
│    → Optional but recommended for 30%+ missing columns        │
│    → Creates: col_was_missing = 1 if NaN, else 0              │
│    → Tells the model "this value was absent" as a signal       │
└─────────────────────────────────────────────────────────────────┘
```

---

### RULE 4 — ML MODEL COMPATIBILITY

```
┌─────────────────────────────────────────────────────────────────┐
│  Tree-based (XGBoost, LightGBM, CatBoost, RandomForest):       │
│    → Can handle NaN natively                                   │
│    → Still recommended: create indicator flags for MNAR        │
│                                                                 │
│  Linear Models (LogReg, LinearReg, Ridge, Lasso):              │
│    → MUST impute — zero NaN tolerance                          │
│                                                                 │
│  Neural Networks / Deep Learning:                               │
│    → MUST impute — no NaN tolerance                            │
│                                                                 │
│  SVM, KNN Classifier:                                           │
│    → MUST impute — no NaN tolerance                            │
│                                                                 │
│  ⚠️  UNIVERSAL RULE FOR ALL MODELS:                             │
│    → Split train/test FIRST                                    │
│    → Fit imputer on TRAIN only                                 │
│    → Transform both TRAIN and TEST using fitted imputer        │
│    → Never fit on full dataset — causes data leakage           │
└─────────────────────────────────────────────────────────────────┘
```

---

## PHASE 4 — PYTHON IMPLEMENTATION BLUEPRINT

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────────
# STEP 0 — Load and copy DATA()
# ─────────────────────────────────────────────────────────────────
df = DATA().copy()

# ─────────────────────────────────────────────────────────────────
# STEP 1 — Standardize disguised missing values
# ─────────────────────────────────────────────────────────────────
DISGUISED_NULLS = ["?", "N/A", "n/a", "unknown", "none", "—", "-", ""]
df.replace(DISGUISED_NULLS, np.nan, inplace=True)

# ─────────────────────────────────────────────────────────────────
# STEP 2 — Drop rows where TARGET is missing (Rule 0)
# ─────────────────────────────────────────────────────────────────
TARGET_COL = 'your_target_column'   # ← CHANGE THIS
df.dropna(subset=[TARGET_COL], axis=0, inplace=True)

# ─────────────────────────────────────────────────────────────────
# STEP 3 — Separate features and target
# ─────────────────────────────────────────────────────────────────
X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

# ─────────────────────────────────────────────────────────────────
# STEP 4 — Train / Test Split BEFORE any imputation
# ─────────────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ─────────────────────────────────────────────────────────────────
# STEP 5 — Define column groups (fill these after Phase 1-2)
# ─────────────────────────────────────────────────────────────────
num_cols_symmetric  = []   # → Mean imputation
num_cols_skewed     = []   # → Median imputation
cat_cols_low_card   = []   # → Mode imputation
cat_cols_high_card  = []   # → 'Unknown' fill
knn_cols            = []   # → KNN imputation
drop_cols           = []   # → Drop (>60% missing or domain-irrelevant)
mnar_cols           = []   # → Indicator flag + impute

# ─────────────────────────────────────────────────────────────────
# STEP 6 — Drop high-missing or irrelevant columns
# ─────────────────────────────────────────────────────────────────
X_train = X_train.drop(columns=drop_cols, errors='ignore')
X_test  = X_test.drop(columns=drop_cols, errors='ignore')

# ─────────────────────────────────────────────────────────────────
# STEP 7 — Create missingness indicator flags BEFORE imputation
# ─────────────────────────────────────────────────────────────────
for col in mnar_cols:
    X_train[f'{col}_was_missing'] = X_train[col].isnull().astype(int)
    X_test[f'{col}_was_missing']  = X_test[col].isnull().astype(int)

# ─────────────────────────────────────────────────────────────────
# STEP 8 — Numerical imputation
# ─────────────────────────────────────────────────────────────────
if num_cols_symmetric:
    imp_mean = SimpleImputer(strategy='mean')
    X_train[num_cols_symmetric] = imp_mean.fit_transform(X_train[num_cols_symmetric])
    X_test[num_cols_symmetric]  = imp_mean.transform(X_test[num_cols_symmetric])

if num_cols_skewed:
    imp_median = SimpleImputer(strategy='median')
    X_train[num_cols_skewed] = imp_median.fit_transform(X_train[num_cols_skewed])
    X_test[num_cols_skewed]  = imp_median.transform(X_test[num_cols_skewed])

# ─────────────────────────────────────────────────────────────────
# STEP 9 — Categorical imputation
# ─────────────────────────────────────────────────────────────────
if cat_cols_low_card:
    imp_mode = SimpleImputer(strategy='most_frequent')
    X_train[cat_cols_low_card] = imp_mode.fit_transform(X_train[cat_cols_low_card])
    X_test[cat_cols_low_card]  = imp_mode.transform(X_test[cat_cols_low_card])

if cat_cols_high_card:
    X_train[cat_cols_high_card] = X_train[cat_cols_high_card].fillna('Unknown')
    X_test[cat_cols_high_card]  = X_test[cat_cols_high_card].fillna('Unknown')

# ─────────────────────────────────────────────────────────────────
# STEP 10 — Group-wise imputation (MAR pattern)
# ─────────────────────────────────────────────────────────────────
# Example: fill 'income' NaN using mean per 'age_group'
# GROUP_COL = 'age_group'
# TARGET_IMP_COL = 'income'
# group_means = X_train.groupby(GROUP_COL)[TARGET_IMP_COL].mean()
# X_train[TARGET_IMP_COL] = X_train[TARGET_IMP_COL].fillna(
#     X_train[GROUP_COL].map(group_means)
# )
# X_test[TARGET_IMP_COL] = X_test[TARGET_IMP_COL].fillna(
#     X_test[GROUP_COL].map(group_means)
# )

# ─────────────────────────────────────────────────────────────────
# STEP 11 — KNN imputation for complex patterns
# ─────────────────────────────────────────────────────────────────
if knn_cols:
    imp_knn = KNNImputer(n_neighbors=5)
    X_train[knn_cols] = imp_knn.fit_transform(X_train[knn_cols])
    X_test[knn_cols]  = imp_knn.transform(X_test[knn_cols])

# ─────────────────────────────────────────────────────────────────
# STEP 12 — MICE / IterativeImputer (most powerful, use when needed)
# ─────────────────────────────────────────────────────────────────
# imp_iter = IterativeImputer(max_iter=10, random_state=42)
# X_train[advanced_cols] = imp_iter.fit_transform(X_train[advanced_cols])
# X_test[advanced_cols]  = imp_iter.transform(X_test[advanced_cols])

# ─────────────────────────────────────────────────────────────────
# STEP 13 — Final validation
# ─────────────────────────────────────────────────────────────────
remaining_train = X_train.isnull().sum()
remaining_test  = X_test.isnull().sum()

assert remaining_train.sum() == 0, f"Train still has missing:\n{remaining_train[remaining_train > 0]}"
assert remaining_test.sum()  == 0, f"Test still has missing:\n{remaining_test[remaining_test > 0]}"

print("✅ No missing values remain. DATA() is ML-ready.")
print(f"   Train shape: {X_train.shape} | Test shape: {X_test.shape}")
```

---

## PHASE 5 — SYNTHESIS & DECISION REPORT

After completing Phases 1–4, deliver this exact report:

```
═══════════════════════════════════════════════════════════════
  MISSING VALUE TREATMENT REPORT
═══════════════════════════════════════════════════════════════

1. DATASET SUMMARY
   Shape         :
   Total missing :
   Target col    :
   ML task       :
   Model type    :

2. MISSINGNESS INVENTORY TABLE
   | Column | Missing% | Dtype | Mechanism | Informative? | Treatment |
   |--------|----------|-------|-----------|--------------|-----------|
   | ...    | ...      | ...   | ...       | ...          | ...       |

3. DECISIONS LOG
   [Column]: [Reason for chosen treatment]
   [Column]: [Reason for chosen treatment]

4. COLUMNS DROPPED
   [Column] — Reason: [e.g., 72% missing, not domain-critical]

5. INDICATOR FLAGS CREATED
   [col_was_missing] — Reason: [MNAR suspected / high missing %]

6. IMPUTATION METHODS USED
   [Column(s)] → [Strategy used + justification]

7. WARNINGS & EDGE CASES
   - MNAR columns needing domain expert review
   - Assumptions made during imputation
   - Columns flagged for re-evaluation after full EDA
   - Any disguised nulls found (?, N/A, 0, etc.)

8. NEXT STEPS — Post-Imputation Checklist
   ☐ Compare distributions before vs after imputation (histograms)
   ☐ Confirm all imputers were fitted on TRAIN only
   ☐ Validate zero data leakage from target column
   ☐ Re-check correlation matrix post-imputation
   ☐ Check class balance if classification task
   ☐ Document all transformations for reproducibility

═══════════════════════════════════════════════════════════════
```

---

## CONSTRAINTS & GUARDRAILS

```
✅ MUST ALWAYS:
   → Work on df.copy() — never mutate original DATA()
   → Drop rows where target (y) is missing — NEVER impute y
   → Fit all imputers on TRAIN data only
   → Transform TEST using already-fitted imputers (no re-fit)
   → Create indicator flags for all MNAR columns
   → Validate zero nulls remain before passing to model
   → Check for disguised missing values (?, N/A, 0, blank, "unknown")
   → Document every decision with explicit reasoning

❌ MUST NEVER:
   → Impute blindly without checking distributions first
   → Drop columns without checking their domain importance
   → Fit imputer on full dataset before train/test split (DATA LEAKAGE)
   → Ignore MNAR columns — they can severely bias the model
   → Apply identical strategy to all columns
   → Assume NaN is the only form a missing value can take
```

---

## QUICK REFERENCE — STRATEGY CHEAT SHEET

| Situation | Strategy |
|-----------|----------|
| Target column (y) has NaN | Drop rows — never impute |
| Column > 60% missing | Drop column (or indicator + expert review) |
| Numerical, symmetric dist | Mean imputation |
| Numerical, skewed dist | Median imputation |
| Numerical, time-series | Forward fill / Interpolation |
| Categorical, low cardinality | Mode imputation |
| Categorical, high cardinality | Fill with 'Unknown' category |
| MNAR suspected (any type) | Indicator flag + domain review |
| MAR, conditioned on group | Group-wise mean/mode |
| Complex multivariate patterns | KNN Imputer or MICE |
| Tree-based model (XGBoost etc.) | NaN tolerated; still flag MNAR |
| Linear / NN / SVM | Must impute — zero NaN tolerance |

---

*PROMPT() v1.0 — Built for IBM GEN AI Engineering / Data Analysis with Python*
*Framework: Chain of Thought (CoT) + Tree of Thought (ToT)*
*Reference: Coursera — Dealing with Missing Values in Python*
