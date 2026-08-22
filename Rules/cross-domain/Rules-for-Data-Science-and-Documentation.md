# Rules for Data Science and Documentation

This document synthesizes technical rules, syntax requirements, and constraints from various segments of a larger body of work, providing a unified and de-duplicated master list.

**Generated on:** October 1, 2025 at 2:20 PM CDT

---

## 1. General Principles

* Break down complex problems into smaller, manageable parts.
* Follow a scientific approach: posit a model, use it, then check if it matches the data or has flaws.

## 2. Data Handling & Preprocessing

* **Probabilities:** Probabilities `p(x)` must be between 0 and 1.
* **Categorical Response:** Categorical response `Y` values must be between 0 and 1 (or `0` to `k-1` for multiclass).
* **GLM Data:** Generalized Linear Model (GLM) response families must belong to a parametric family (e.g., binomial, gaussian, poisson, gamma).
* **Poisson Regression Data:** Poisson Regression is appropriate for counts without an upper limit.
* **Histogram Data:** Histogram data requires values that can be binned.
* **Kernel Density Estimation Data:** Kernel Density Estimation data requires variables for which a kernel function can be applied.
* **PCA Data Centering:** For Principal Component Analysis (PCA), data must be centered (each variable has mean 0).
* **PCA Data Scaling:** Scale PCA variables to unit variance (standardize) when variables have different, incomparable scales.
* **Factor Analysis Data:** For Factor Analysis, observable variables must have mean zero and variance 1 (achieved by centering and standardizing).
* **Factor Analysis Latent Factors:** For Factor Analysis, latent factors must have mean zero and variance 1.
* **Thomson Sampling Data Assumptions:** For Thomson Sampling, latent variables `A_k` must be totally independent, mean 0, variance 1. Noises `eta_j` must be independent of each other and `A_k`.
* **Partial Successes:** Recode partial successes (`outcome = 0.5`) as 1.0 or 0 before fitting a model with a logistic link function; explain and justify the choice.
* **Massive Datasets:** For massive datasets where additive models are computationally prohibitive, consider random subsets to estimate bias from linear models.
* **Data Loading (R):** Load the data set from Homework 1 as a data frame named `mobility`.
* **Data Filtering (R):** Do not remove any row from the `mobility` data frame that has complete values for `Mobility`, `Population`, and `State`.
* **`MAPE` Column Creation:** Add a new column, `MAPE`, calculated as `Price / Earnings_10MA_back`; it must meet specific summary statistics (Min: 4.785, 1st Qu: 11.710, Median: 15.950, Mean: 16.550, 3rd Qu: 19.960, Max: 44.200, NAs: 120).

## 3. Model Specification & Definition

* **Additive Model Centering:** When fitting additive models, ensure partial response functions (`f_j(x_j)`) are centered (e.g., `E[f_j(X_j)] = 0`) to ensure identifiability of the intercept.
* **Additive Model Form:** The Additive Model Form is `E[Y|X=F] = a + sum(f_i(x_i))`.
* **Linear Model Form:** The Linear Model Form is `E[Y|X=F] = beta_0 + sum(beta_j * x_j)`.
* **Linear Model Intercept:** In Linear Models, the `x_0` predictor variable must always be the constant 1 to handle the intercept as a regression coefficient.
* **Linear Model Partial Residual:** The partial residual for `X_k` in Linear Models is the difference between `Y` and its expectation, ignoring `X_k`'s contribution.
* **Additive Model Partial Residual:** The partial residual for `X_k` in Additive Models is `Y_k_partial = Y - (a + sum_{j!=k} f_j(x_j))`.
* **Additive Model with Interactions:** The Additive Model with Interactions (Second-Order Expansion) is `mu(x) = a + sum(f_i(x_i)) + sum_{j<k} f_jk(x_j, x_k)`.
* **Interaction Term Identifiability:** For interaction terms in additive models, insist that `E[f_jk(X_j, X_k)] = 0` for all `j,k` for identifiability.
* **Purely Interactive Contributions:** To represent purely interactive contributions, insist that second-order `f_jk` functions are uncorrelated with (orthogonal to) first-order `f_j` and `f_k` functions.
* **Varying-Coefficient Model Form:** The Varying-Coefficient Model Form is `mu(x) = a + sum(X_j * f_j(X_neg_j))`.
* **Parametric Regression Model Form:** The Parametric Regression Model Form is `Y = f(X; theta) + epsilon`.
* **Logistic Regression Model Form:** The Logistic Regression Model Form is `log(p(x) / (1 - p(x))) = beta_0 + x * beta`.
* **Multiclass Logistic Regression Probability:** For `k` classes, `Pr(Y=c|X=x) = exp(beta_0c + x * beta_c) / sum_{l=0 to k-1} exp(beta_0l + x * beta_l)`.
* **Multiclass Logistic Regression Identifiability:** For Multiclass Logistic Regression identifiability, fix one class's parameters (e.g., `c=0`) to zero.
* **Generalized Linear Model Components:** Generalized Linear Models (GLM) require: (1) a linear predictor `eta(x) = beta_0 + x * beta`, (2) a link function `g` such that `eta(x) = g(mu(x))`, and (3) a dispersion scale function `V` such that `V[Y|X=x] = phi * V(mu(x))`.
* **OLS as GLM:** For Ordinary Least Squares (OLS) as a GLM, use identity link `g(mu) = mu` and constant variance `V(mu) = 1`.
* **Poisson Regression Link:** For Poisson Regression, a natural link function is `g(mu) = log(mu)`.
* **Overdispersion Modeling:** If `V[Y|X=x]` does not track `V(mu(x))`, model overdispersion as `V[Y|X=x] = phi * V(mu(x))`.
* **`Mobility` Definition:** `Mobility` is defined as the probability that a child born in 1980-1982 into the lowest income quintile will be in the top quintile at age 30.
* **National Mobility Level:** "National mobility level" is defined as the average mobility across communities, weighted by population.
* **`Returns` Definition:** "Returns" refers to `Return_10_fwd` throughout.
* **`ethnic-dominance` in GAM:** The `ethnic-dominance` variable must be included in Generalized Additive Models (GAMs) as a factor (`as.factor`).
* **`npreg` Interactions:** The `npreg()` function automatically includes interactions between all variables specified in its formula.
* **Model Identifiability:** Always ensure models are identifiable to obtain meaningful and unique parameter estimates.
* **Parametric Model Preference:** Prefer parametric models if scientific theory asserts linear relationships or prediction benefits from lower variance with small samples, provided the model is well-specified.

## 4. Algorithm & Procedure

* **Program Functionality:** Verify program functionality.
* **Back-fitting Input `x` (Linear):** For Back-fitting for Linear Models, input `x` must be `n x (p+1)` with the 0th column all 1s.
* **Back-fitting Input `y` (Linear):** For Back-fitting for Linear Models, input `y` must be `n x 1`.
* **Back-fitting Tolerance `epsilon`:** For Back-fitting algorithms, input `epsilon` (tolerance) must be `> 0`.
* **Back-fitting Preprocessing (Linear):** For Back-fitting for Linear Models, center `y` and each column of `x` during preprocessing.
* **Back-fitting Initialization (Linear):** For Back-fitting for Linear Models, initialize `beta_j = 0` for `j = 0:p`.
* **Back-fitting Loop Condition (Linear):** For Back-fitting for Linear Models, repeat until `|beta_j - old_beta_j| < epsilon` for all `j`.
* **Back-fitting Loop Assumption (Linear):** For Back-fitting for Linear Models, assume at least one pass through the loop is made.
* **Back-fitting Intercept (Linear):** For Back-fitting for Linear Models, calculate the intercept `beta_0` only once, at the end, due to data centering.
* **Back-fitting Input `x` (Additive):** For Back-fitting for Additive Models, input `x` must be an `n x p` matrix.
* **Back-fitting Input `y` (Additive):** For Back-fitting for Additive Models, input `y` must be an `n x 1` matrix.
* **Back-fitting Smoother (Additive):** For Back-fitting for Additive Models, a one-dimensional smoother is required.
* **Back-fitting Initialization (Additive):** For Back-fitting for Additive Models, initialize `f_j = 0` for `j = 1:p`.
* **Back-fitting Loop Condition (Additive):** For Back-fitting for Additive Models, repeat until `|f_j - old_f_j| < epsilon` for all `j`.
* **Back-fitting Partial Residual (Additive):** In Additive Model Back-fitting, calculate partial residual `Y_k_partial = Y - sum_{j!=k} f_j(x_jk)` for each `k`.
* **Back-fitting Smoothing (Additive):** In Additive Model Back-fitting, smooth `Y_k_partial` on `x_k` to get `f_k`.
* **Back-fitting Centering (Additive):** In Additive Model Back-fitting, ensure `f_k` is centered (`f_k = f_k - mean(f_k)`).
* **GLM Specification Test Procedure:** The GLM Specification Test Procedure (Ch. 10 Basic Procedure) steps must be followed: (1) Get data, (2) Fit parametric model, get `theta_hat` and `MSE_p(theta_hat)`, (3) Fit nonparametric regression, get `eta_hat` and `MSE_np(eta_hat)`, (4) Calculate `T = MSE_p(theta_hat) - MSE_np(eta_hat)`, (5) Simulate from parametric model (`theta_hat`) to get faked data `(x_i^*, y_i^*)`, fit parametric and nonparametric models to simulated data, calculate `T^*`, (6) Repeat step 5 many times for `T^*` distribution, (7) Calculate p-value: `p_value = (1 + sum(T^* >= T_obs)) / (1 + num_replicates)`.
* **Kernel Bandwidth Re-tuning:** For `calc.T` (and generally for kernel methods), kernel bandwidth must be re-tuned for each new data set.
* **GLM IRWLS Algorithm:** The GLM Iteratively Re-weighted Least Squares (IRWLS) Algorithm must follow these steps: (1) Initialize `beta_0`, `beta`, (2) Repeat until `beta_0`, `beta` converge: (a) Calculate `eta(x_i)` and `mu(x_i)`, (b) Find `z_i = eta(x_i) + (y_i - mu(x_i)) * g'(mu(x_i))`, (c) Calculate `w_i = 1 / ((g'(mu(x_i)))^2 * V(mu(x_i)))`, (d) Perform weighted linear regression of `z_i` on `x_i` with `w_i` to get new `beta_0`, `beta`.
* **GLM IRWLS Effective Response:** For GLM IRWLS, the effective response is `z = g(mu) + (Y - mu) * g'(mu)`.
* **GLM IRWLS Weights:** For GLM IRWLS, weights `w` must be inversely proportional to the variance `V[Z|X=x] = (g'(mu))^2 * V[Y|X=x]`.
* **Logistic Regression IRWLS Weights:** For Logistic Regression in IRWLS, weights at `x` must be proportional to `mu(x) * (1 - mu(x))`.
* **Poisson Regression IRWLS Weights:** For Poisson Regression in IRWLS, weights `w` are proportional to `mu`.
* **Simulating from Kernel Density Estimates:** To simulate from Kernel Density Estimates: (1) Pick integer `i` uniformly at random from `1` to `n` (with replacement), (2) Draw a new value from kernel `K` centered at `x_i` with bandwidth `h`.
* **Simulating from Joint Kernel Density Estimates:** To simulate from Joint Kernel Density Estimates, pick a random data point, then draw each coordinate independently from the kernel distribution centered on that point.
* **Simulating from Conditional Kernel Density Estimates:** To simulate from Conditional Kernel Density Estimates, select data point `i` with weight proportional to `K_X((x - x_i)/h_X)`, then generate `Y` from `K_Y` centered at `y_i`.
* **Simulating from Histogram Estimates:** To simulate from Histogram Estimates: (1) Randomly pick a bin (multinomial distribution, weights proportional to bin counts), (2) Draw from a uniform distribution over the selected bin's range.
* **Neyman's Smooth Test Procedure:** Neyman's Smooth Test Procedure must follow these steps: (1) Transform data `x_i` to `y_i = F(x_i)` (if testing against `F`), or use data directly (if testing for uniformity), (2) Estimate `theta_hat` (or calculate `h_j_bar`), (3) Compute test statistic (e.g., `ChiSq = n * sum(h_j_bar^2)`), (4) If `d` is data-driven, bootstrap from `Unif(0,1)` for null distribution and p-value. If `d` is fixed, compare to `ChiSq(d)` distribution.
* **Smooth Test with Estimated Parameters:** For Smooth Tests with estimated parameters, use Maximum Likelihood Estimates (MLEs) (`beta_hat`) before transforming data `y_i = F(x_i; beta_hat)`.
* **Relative Distribution Estimation (F0 known):** If `F0` is known, estimate relative distribution `g` using series expansions or kernel density estimation on transformed `y_i`.
* **Relative Distribution Estimation (F0 unknown):** If `F0` is unknown but samples from both are available, estimate `Q_0` (e.g., empirical quantile function), then apply a known-`F0` estimation method.
* **Relative Distribution Uncertainty:** Assess relative distribution uncertainty using bootstrap, including `Q_0` uncertainty if estimated.
* **MA(1) Model Estimation:** When estimating an MA(1) model, use an AR(1) model as the auxiliary function.
* **Linear Regression of Mobility:** Run a linear regression of mobility against all appropriate covariates.
* **Exclude `ID` from Mobility Regression:** Exclude the `ID` variable from the regression of mobility.
* **Linear Regression of Growth Rate:** Linearly regress growth rate on undervaluation index and log of GDP.
* **`year` in Regression:** Use `factor(year)` in regression formulas, not `year`.
* **Predictive Comparisons:** In "Average predictive comparisons," do not re-fit either model.
* **Returns Regressions:** Run four linear regressions for returns: on Price, on Earnings, on both Price and Earnings, and on both with interaction.
* **`MAPE` Regression:** Linearly regress returns on `MAPE` (and nothing else).
* **`1/MAPE` Regression:** Linearly regress returns on `1/MAPE` (and nothing else); do not add a new column or vector for `1/MAPE`.
* **`MAPE` and `1/MAPE` Regression:** Linearly regress returns on both `MAPE` and `1/MAPE` (without interaction).
* **Quadratic `MAPE` Regression:** Linearly regress returns on `MAPE`, `1/MAPE`, and `MAPE^2`.
* **Kernel Regression of Returns:** Use `npreg` to estimate a kernel regression of returns on `MAPE`.
* **Extra Credit Kernel Regression:** For extra credit, run kernel regression of returns on `Price` and `Earnings_10MA_back`, but *not* `MAPE`.
* **Extra Credit Optimal Levels:** (Extra Credit) Mathematically show optimal `levels` are two weighted averages of `Mobility`, and find them using two calls to `weighted.average` without `WSE`, `dixie.fit`, `dixie.WSE`, or optimization.
* **Log Mass Regression:** Linearly regress log of new mass on log of ancestral mass.
* **Spline Regression of Log Mass:** Use a smoothing spline for nonparametric regression of log new mass on log ancestral mass.
* **Logistic Regression for Civil War:** Fit logistic regression for civil war on all variables except `country` and `year`, including a quadratic term for `exports`.
* **War Prediction Rule:** Predict war if probability > 0.5, and peace otherwise.
* **Calibration Plot Data Grouping:** For calibration plots, divide data points into groups based on predicted civil war probability ranges.
* **GAM for Civil War:** Fit a GAM with the same variables as logistic regression, smoothing all continuous predictors, and *not* including an explicit quadratic `exports` term.
* **GAM `year` Predictor:** Include `year` as a predictor variable in the GAM.
* **GAM Categorical Variables:** Use a GAM with a logistic link function, smooth all continuous predictors, and include all categorical variables (except `campaign` and `country` names) by default. Justify departures.

## 5. Statistical Inference & Interpretation

* **Invalid Inference:** Inferential statistics (p-values, confidence sets) become invalid if the same data is used for both model selection and inference.
* **Valid Inference after Selection:** To perform valid statistical inference after model selection, use an independent data set: one part to select the model, and the other part for re-estimating the selected model and inferential statistics.
* **Significance vs. Importance:** Do not interpret statistical significance as scientific or real-world significance.
* **Significant Coefficient Implication:** Do not conclude a variable influences the response solely based on a significant regression coefficient.
* **Insignificant Coefficient Implication:** Do not conclude a variable does not influence the response solely based on an insignificant regression coefficient.
* **Causal Inference Caution (Regression):** Do not use regression thoughtlessly for causal inference; it is primarily for probabilistic prediction.
* **Prediction Change Caution:** Do not predict response changes by simple plugging into a regression model, unless specific causal assumptions hold.
* **Parameter Interpretation Caution:** Be aware that model misspecification can lead to inaccurate interpretation of coefficients.
* **Nonlinear Model Interpretation:** For nonlinear or interactive regression models, do not assume the predictive relationship between an input `U` and output `Y` can be boiled down to a single number; it depends on context (starting, ending, and contextual values of `U` and other variables `V`).
* **High P-value Meaning:** A high p-value does not mean a model is correct, only that there isn't enough evidence to reject it.
* **R Default Statistics:** Do not assume R’s default standard errors or p-values on estimated regression coefficients are trustworthy for inferential statistics.
* **Uncertainty Assessment:** Assess uncertainty using suitable bootstrap or simulation procedures.

## 6. Model Assessment & Validation

* **Prediction Evaluation:** When evaluating predictions, minimize the expected error (risk or generalization error) on new data.
* **Validation Data Use:** Do not use validation data in model estimation when seeking an unbiased estimate of generalization error.
* **K-fold CV Data Division:** For k-fold cross-validation, divide data into `k` equally-sized subsets randomly.
* **K-fold CV Test Set Usage:** For k-fold cross-validation, each subset must be used as the test set exactly once.
* **Linear Regression Residuals:** If using linear regression with standard assumptions for inference, always test whether the residuals are white noise (Gaussianity, homoskedasticity, lack of correlation). Failure to do so invalidates the inference.
* **Model Error:** Do not assume that all models should have zero error.
* **In-sample vs. Generalization Error:** Do not assume that in-sample loss is a good approximation to generalization error when the model was specifically picked to match training data.
* **Model Assumptions:** Always check the validity of a model's assumptions.
* **Calibration Check (Range-based):** For range-based calibration checks, if predicted probability is in `[p, p + epsilon)`, the observed relative frequency must also be in that range.
* **Calibration Check (Scoring Rule):** For calibration checks, use a proper scoring rule (e.g., Brier score, negative log-likelihood) that minimizes when predictions are calibrated, evaluating out-of-sample or via cross-validation.
* **GLM/GAM Specification Test:** To perform a GLM/GAM Specification Test, fit both models to data, simulate from GLM, re-fit both to simulated data repeatedly, then compare deviance differences.
* **Nonparametric Regression for Model Checking:** Use nonparametric regression for model checking, as it effectively checks for all kinds of systematic errors.
* **Tree Growing Stopping:** For tree growing, avoid stopping too early; use cross-validation and pruning rather than arbitrary thresholds.
* **Tree Pruning Goal:** For tree pruning, find the optimal number of leaves that generalizes best by checking if extra capacity improves generalization error.
* **Cross-Entropy:** Cross-entropy is a better metric than misclassification rate for comparing models, as it minimizes the difference between model-predicted and true probabilities.
* **Binary Classification Rule (Misclassification Rate):** For binary classification to minimize misclassification rate, predict `Y = 1` when `p > 0.5` and `Y = 0` when `p < 0.5`.
* **Classification Tree Prediction:** For classification tree point forecasts, strategy depends on loss function; for misclassification rate, predict the most probable class. For distributional predictions, use empirical relative frequencies in leaf nodes (with caution for small samples/many classes).
* **Neyman-Pearson Approach (Binary Classification):** For binary classification, the Neyman-Pearson approach fixes a limit `alpha` on false positive probability and minimizes false negative rate among tests of size `alpha`.
* **Logistic Regression Residuals:** For logistic regression, redefine and check residuals (response or Pearson); they should be unpredictable from covariates, and Pearson residuals should have constant variance.
* **Model Comparison (Predictive Accuracy):** For model comparisons of predictive accuracy, do not use R’s default significance tests or R-squared; use suitable bootstrap or cross-validation.
* **Leave-One-Out CV:** Use leave-one-out cross-validation to find model Mean Squared Errors (MSEs), and identify which predicts better and by how much.
* **Kernel vs. Linear Performance:** Compare kernel regression's predictive performance to the linear model with the same variables.
* **Linear Regression R-squared Comparison:** For linear regression `R^2` values, assess if they can be meaningfully compared and identify the preferred model if so.
* **Generalization Error Comparison:** For generalization error from five-fold cross-validation, assess if values can be meaningfully compared and identify the preferred model if so.
* **Confidence Limit Compatibility:** Assess compatibility of confidence limits from resampling residuals vs. cases, and explain which seems best if not compatible.
* **Kernel Regression Prediction Character:** Compare kernel regression predictions to previous models and describe if they are "slightly wiggly copies" or qualitatively different.
* **Inferential Statistics Reliability:** Assess the reliability of inferential statistics calculated in Homework 1.
* **`WSE` Function Check:** Check that `WSE` returns MSE when all weights are equal.
* **Logistic Regression Specification Test:** Test logistic regression specification using GAM as alternative model; report p-value and explain model preference.
* **Logistic Regression Prediction Accuracy:** Calculate the fraction of correct predictions for logistic regression and a "no war" pundit.
* **Calibration Plot Assessment:** For the calibration plot, assess if it follows the 45-degree diagonal (and if it should), and if observed frequencies increase with predicted probability.
* **GAM Prediction Accuracy:** Report GAM's fraction of accurate predictions and compare to logistic regression and "peace-always" pundit.
* **GAM Calibration Plot:** Compare GAM's calibration plot to logistic regression's plot regarding tracking actual frequencies.

## 7. Code & R Programming

* **Code Readability:** Code must be formatted, organized, indented, use meaningful names, and include comments for readability.
* **Code Redundancy:** Avoid redundant code; consolidate common parts into a single implementation, including only computations necessary to answer analytical questions.
* **Function Granularity:** Break code into many short, meaningful functions.
* **Borrowed Code:** Explicitly acknowledge and source borrowed code in comments.
* **Function Testing:** Functions or procedures not directly from notes must have accompanying tests.
* **Runnable Code:** All submitted code must run successfully.
* **R Markdown/Knitr:** If using R Markdown/knitr, the Markdown file must knit successfully, and both knitted and source files must be submitted.
* **Separate `.R` Files:** If submitting a separate `.R` file, clearly label computations via comments to link to specific claims or results.
* **Obscure Code:** Avoid excessively obscure one-line code.
* **`npreg` Caching:** When using R Markdown for computation-intensive `npreg` calls, consider caching the code.

### 7.1. R Base Functions & General Syntax

* **RNG Naming:** Default R random number generator functions (e.g., `rnorm`, `runif`, `rexp`, `rpois`, `rbinom`) start with "r".
* **RNG First Argument:** The first argument for R random number generator functions must be the number of draws to make.
* **RNG Subsequent Arguments:** Subsequent arguments for R random number generator functions must be the parameters of the distribution.
* **RNG Vectorization:** R random number generator parameters can be vectorized.
* **`sample()` `x`:** For `sample()`, `x` must be a vector.
* **`sample()` `size`:** For `sample()`, `size` must be the number of samples desired.
* **`sample()` `replace`:** For `sample()`, the `replace` argument must be `TRUE` or `FALSE`.
* **`sample()` `replace=FALSE` `size`:** If `replace` is `FALSE` in `sample()`, `size` must not exceed the length of `x`.
* **`sample()` `replace=TRUE` `size`:** If `replace` is `TRUE` in `sample()`, `size` can be arbitrarily larger than the length of `x`.
* **`sample()` `prob`:** For `sample()`, the `prob` argument should be a vector of probabilities with the same length as `x`.
* **`sample()` `prob` Normalization:** If `prob` elements in `sample()` (or multinomial sampling) are positive but do not sum to 1, they will be normalized by their sum.
* **`replicate()` `expr`:** For `replicate(n, expr)`, `expr` must be an executable R expression.
* **`replicate()` `n`:** For `replicate(n, expr)`, `n` must be the number of times to repeat the expression.
* **`lm()` Syntax:** The syntax `lm(y ~ x, weights = 1/(1 + 0.5 * x^2))` is used for weighted least squares in R.
* **`read.csv()`/`scan()`:** Use `read.csv()` for CSV files and `scan()` for other data files in R.
* **`na.omit()`:** Use `na.omit()` to remove rows with NA values in R.
* **Data Subsetting:** Use `data_frame[data_frame$column == value, ]` for data subsetting in R.
* **`lm()` Use:** Use `lm(response ~ predictors, data = data_frame)` for linear models in R.
* **`summary()` Use:** Use `summary()` for summary statistics, suppressing `signif.stars` and setting `digits` as needed.
* **`density()`:** Use `density()` from base R for one-dimensional Kernel Density Estimation (defaults to Gaussian kernels with rule-of-thumb bandwidth).
* **`prcomp()`:** Use `prcomp()` from base R for PCA.
* **`prcomp()` Scaling:** For `prcomp()`, set `scale. = TRUE` to standardize variables to unit variance.
* **`prcomp()` Loadings:** Access PCA loadings via `pca_object$rotation`.
* **`biplot()`:** Use `biplot(pca_object)` for biplots of PCA results.
* **`factanal()`:** Use `factanal()` from base R for Factor Analysis.
* **`factanal()` `factors`:** For `factanal()`, set the `factors` argument to the desired number of factors.
* **`factanal()` `scores`:** For `factanal()`, specify `scores="regression"` for the Thomson estimator.
* **`factanal()` Default Test:** `factanal()` automatically runs a likelihood ratio test assuming Gaussian distributions.
* **`rbinom()`:** `rbinom()` simulates binary outcomes.
* **`rnorm()`:** `rnorm()` simulates Gaussian noise.
* **`ilogit()`:** `ilogit()` is the inverse logit function.
* **`optim()` Arguments:** The `optim` function's `fn` argument must be a function, and `par` must be an initial guess for parameters.

### 7.2. R Package Specifics

* **Sampling Data Frames:** When sampling rows from a data frame, sample row numbers (e.g., `df[sample(1:nrow(df), size = b), ]`).
* **`np` package messages:** To suppress `np` package progress messages, set `options(np.messages=FALSE)`.
* **`npreg()` Function:** The `npreg()` function (from the `np` package) requires a `formula` argument (specifying the model) and a `data` argument (a data frame containing variables in the formula).
* **`npreg()` Interactions:** `npreg()` does not require or recognize specific notation for interactions.
* **`npreg()` Intercepts:** `npreg()` does not require or recognize specific inclusion/exclusion of intercepts.
* **`npreg()` Categorical Variables:** To include categorical variables in `npreg()` formulae, wrap the variable in `factor()`.
* **`npreg()` Ordered Variables:** To include ordered variables in `npreg()` formulae, wrap the variable in `ordered()`.
* **`npreg()` Tolerances:** Adjust `npreg()` bandwidth optimization tolerances (`tol` for bandwidths, `ftol` for MSE) to improve speed. A rule of thumb is to start both at `0.01`. (Note: specific problem contexts may require different values, e.g., `tol` 10, `ftol` 10^-4).
* **`smooth.spline()` `predict()`:** `predict()` for `smooth.spline` expects a vector named `x`.
* **`smooth.spline()` `predict()` Return:** `predict()` for `smooth.spline` returns a list with an `x` component (in increasing order) and a `y` component.
* **`smooth.spline()` CV:** `smooth.spline(x, y, cv = FALSE)` uses Generalized Cross-Validation (GCV) by default; set `cv = FALSE` for leave-one-out cross-validation.
* **`gam()` Use:** Use `gam()` from `mgcv` or `gam` package for Additive Models.
* **`gam()` Smoothed Terms:** Use `s(variable)` for smoothed terms in `gam`.
* **`gam()` Joint Smoothing:** Use `s(variable1, variable2)` for joint smoothing/interaction terms in `gam`.
* **`gam()` `s(.)` Limitation:** Cannot use `s(.)` to smooth all variables automatically in `gam`; each `s(variable)` must be listed explicitly.
* **`gam()` Interaction Syntax:** For `gam` interaction terms, use `s(x_j, x_k)` for thin-plate splines (similar scales) or `te(x_j, x_k)` for tensor product splines (different scales).
* **`gam()` Mixed Interaction Syntax:** For `gam` continuous-categorical interactions, use `s(x_j, by=x_k)` or `te(x_j, by=x_k)`.
* **`mgcv` Separated Contributions:** For separated additive and interactive terms in `mgcv`, use `ti(x_j) + ti(x_k) + ti(x_j, x_k)`.
* **`mgcv` Varying-Coefficient Models:** For Varying-Coefficient Models in `mgcv`, use `s(x_k, by=x_j)` with the `by` option.
* **`glm()` Use:** For GLM fitting in R, use the `glm` function and specify the `family` argument (e.g., `"binomial"`, `"gaussian"`, `"poisson"`).
* **`predict()` for Logistic Regression:** For `predict()` with logistic regression, use `type = "response"` to get probabilities (default is log-odds).
* **`tree` Package:** Use `tree(formula, data, ...)` from the `tree` package for Regression Trees.
* **`prune.tree()`:** The `prune.tree` function evaluates tree error and prunings, taking a `best` argument, with default `method="deviance"`.
* **`cv.tree()`:** The `cv.tree` function performs k-fold cross-validation (default `k=10`) for trees.
* **`npudens()`:** Use `npudens()` from `np` package for Joint Density Estimation.
* **`npudens()` Formula:** The `npudens` formula does not use a dependent variable on the left-hand side of `~`.
* **`npplot()` `plot.behavior`:** For `npplot`, setting `plot.behavior = "data"` calculates plotting information without plotting, returning objects for custom plotting.
* **`npcdens()`:** Use `npcdens()` from `np` package for Conditional Density Estimation.
* **`ddst` package:** Use the `ddst` package for Smooth Tests, specifically `ddst.uniform.test`, `ddst.norm.test`, `ddst.exp.test`.
* **`ddst` P-value Calculation:** For `ddst` functions, set `compute.p = TRUE` to calculate p-values (note: computationally expensive).
* **`reldist` package:** Use `reldist()` from `reldist` package for Relative Distributions.
* **`reldist()` Arguments:** For `reldist()`, `y` is the comparison sample, `yo` is the reference sample, and `yolabs` can convert axis labels to original units.
* **`sim.logistic()`:** The `sim.logistic` function requires the `faraway` package and simulates `y = rbinom(n, size=1, prob=ilogit(linear.parts))`.

## 8. Function Design & Implementation

* **`predlims` `prediction.sd`:** The `predlims` function must calculate `prediction.sd = sqrt(preds$se.fit^2 + sigma^2)`.
* **`predlims` Upper Limit:** The `predlims` function must calculate the upper limit as `preds$fit + 2 * prediction.sd`.
* **`predlims` Lower Limit:** The `predlims` function must calculate the lower limit as `preds$fit - 2 * prediction.sd`.
* **Std Dev Combination:** For uncorrelated noise sources, combine standard deviations by "adding in quadrature" (square root of sum of squares).
* **`graymapper` `breaks` Validation:** For the `graymapper` function, if `breaks` is provided, `length(breaks)` must equal `n.levels + 1`.
* **`graymapper` `breaks` ("length"):** For `graymapper` with `break.by = "length"`, `breaks` are `seq(from = min(z), to = max(z), length.out = n.levels + 1)`.
* **`graymapper` `breaks` (other):** For `graymapper` with other `break.by` values, `breaks` are `quantile(z, probs = seq(0, 1, length.out = n.levels + 1))`.
* **`graymapper` Color Assignment:** For the `graymapper` function, darker points must indicate higher values of `z`.
* **`graymapper` Output:** The `graymapper` function must return breakpoints to facilitate using the same scale in multiple maps.
* **`sim.lm` Assumptions:** The `sim.lm` function assumes one input `x` and response `y`, and homoskedastic Gaussian noise.
* **`sim.lm` `sigma` Calculation:** The `sim.lm` function must calculate `sigma_hat = summary(linfit)$sigma * sqrt((n - 2) / n)` for simulation.
* **`sim.lm` Simulation:** The `sim.lm` function must simulate `y_sim = predict(linfit, newdata) + rnorm(n, 0, sigma_hat)`.
* **`sim.lm` `X` Handling:** In `sim.lm`, keep `x` values fixed unless `x` distribution is specified (generate `x`) or vague IID (resample `x`).
* **`ar1.fit`:** Function `ar1.fit` must fit an AR(1) model to a time series using `lm`.
* **`ar1.fit` Return:** Function `ar1.fit` must return intercept, slope, and noise variance.
* **MA(1) Functions:** MA(1) model estimation functions must be analogous to `ma.msm.est` and `ma.msm.objective`.
* **`ma.mm.est` Inputs:** Function `ma.mm.est` must accept two numbers (covariance and variance) as inputs.
* **`ma.mm.objective`:** Function `ma.mm.objective` must calculate the objective function, model-predicted moments, and return the distance between predicted and actual moments.
* **`se.prop`:** Function `se.prop` must take vectors `p` (proportions) and `n` (trial numbers) as inputs, and return a vector of standard errors.
* **`WSE` Signature:** Function `WSE` must take `predicted`, `observed`, and `weights` vectors, calculate `sum(weights * (observed - predicted)^2)`, and return a single real number.
* **`WSE` Defaults:** Function `WSE`'s default for `observed` must be the `Mobility` column, and default for `weights` must be `1 / (standard errors from problem 2)^2`.
* **`dixie`:** Function `dixie` must take a vector of state names and return a binary vector (1 for Confederate state, 0 otherwise).
* **`dixie.fit`:** Function `dixie.fit` must take a data frame with `State` column and `levels` vector, use `dixie` to classify states, and return `levels[1]` for Confederate states or `levels[2]` otherwise.
* **`dixie.WSE`:** Function `dixie.WSE` must take `levels` and a data frame (default `mobility`), predict mobility using `dixie.fit`, use `WSE` with `Mobility` and standard-error-based weights, and return weighted squared error by calling, not re-writing, earlier functions.
* **Problem 7 Optimization Function:** The problem 7 optimization function must take a data frame (default `mobility`) and initial `levels` guess (default `c(0.01,0.15)`), returning *only* the fitted `levels` values.
* **`rmass`:** Function `rmass` must take ancestral mass `X_i`, estimated spline `r`, and other parameters, returning a single random `X_descendant` value in grams between `xmin` and `xmax`.
* **`origin`:** Function `origin` must take ancestral masses, pick `X_i`, generate two independent `X_descendant` values, replace `X_i` with one, add the other to the vector end, ensuring neither returned component matches the ancestral mass.
* **`extinct.prob`:** Function `extinct.prob` must take species masses and parameters `p`, `beta`, returning extinction probabilities according to Eq. A.4.
* **`extinction`:** Function `extinction` must take species masses, `p`, `beta`, returning a possibly-shorter vector with extinct species masses removed, handling total extinction.
* **`evolve_step`:** Function `evolve_step` must take species masses, parameters, and curves, call `origin` and `extinction`, and return a new vector of species masses.
* **`mass_evolve`:** Function `mass_evolve` must take `evolve_step` inputs plus integer `T`, iterate `T` times, and return the final species masses vector.
* **`WSE` MSE Check:** Check that `WSE` returns MSE when all weights are equal.
* **Simulated Spline Check:** Check that a spline curve fit to simulated values (`rmass`) is close to, but not identical with, the spline from data, and explain why.
* **`origin` Output Check:** For problem A.5.5a, verify that for a length-one ancestral mass vector, neither returned component matches the ancestral mass (and explain why), both components have same marginal distribution, and are uncorrelated.

## 9. Dimensionality Reduction (PCA, LLE, Factor Analysis)

* **PCA Numerical Variables:** PCA only works with numerical variables.
* **PCA Objective Equivalence:** In PCA, minimizing mean-squared distance between original vectors and projections is equivalent to maximizing projection variance.
* **PCA Component Orthogonality:** Principal components (eigenvectors of the covariance matrix) must be orthogonal to one another.
* **PCA Eigenvalue Constraint:** Eigenvalues of the PCA covariance matrix must be `>= 0`.
* **PCA R-squared Definition:** PCA R-squared is `(sum of variances of q principal components) / (total variance)`.
* **PCA R-squared for Full Components:** PCA R-squared is `1` if all `p` principal components are used (unless variables are linearly dependent or `n < p`).
* **PCA Interpretation Caution:** Avoid reifying PCA components; they may reflect covariance patterns with many causes or be artifacts of spatial correlations.
* **Factor Model Equation:** The Factor Model Equation is `X = Fw + epsilon`.
* **Factor Model Population Covariance:** The Factor Model Population Covariance is `v = phi + w'w`.
* **Factor Model Identifiability (Degrees of Freedom):** For Factor Model identifiability, the number of independent parameters in `w` and `phi` must not exceed `p(p-1)/2`.
* **Factor Model Rank:** If a factor model with `q` factors holds, the matrix `u = w'w` has rank `q`.
* **Factor Model Rotation Problem:** Factor Model parameters are unidentifiable under orthogonal rotation (the "rotation problem").
* **Factor Model Factor Uncorrelation:** For Factor Analysis, factors must be uncorrelated across individuals and variables.
* **Factor Model Noise Uncorrelation:** For Factor Analysis, noise terms must be uncorrelated across individuals and observable variables.
* **Factor Model Noise-Factor Uncorrelation:** For Factor Analysis, noise terms must be uncorrelated with factor variables.
* **Factor Model Gaussian Assumption:** For Factor Analysis (MLE), factor scores `F_ik` are assumed `N(0,1)`.
* **Factor Model Selection:** For Factor Analysis model selection, use log-likelihood ratio tests to determine the number of factors (`q`), comparing nested models.
* **Factor Model `R^2` Caution:** Do not use `R^2` to assess goodness-of-fit for factor models; use goodness-of-fit tests (e.g., LRT) or cross-validation instead.
* **Factor Model Causal Inference:** Factor Model fit alone does not imply underlying causal structure, due to the rotation problem and model equivalence.
* **LLE Input Data Matrix:** The LLE input data `X` must be an `n x p` matrix.
* **LLE Desired Dimensions:** For LLE, the desired number of dimensions `q` must be less than `p` (`q < p`).
* **LLE Neighbors Parameter Type:** For LLE, the number of local neighbors `k` must be an integer.
* **LLE Neighbors Parameter Constraint:** For LLE, the number of local neighbors `k` must be greater than `q + 1` (`k > q + 1`).
* **LLE Output Matrix:** The LLE output `Y` must be an `n x q` matrix.
* **`lle` Function `q` Constraint 1:** For the `lle` function, `q` must be `> 0`.
* **`lle` Function `q` Constraint 2:** For the `lle` function, `q` must be `< ncol(x)`.
* **`lle` Function `alpha` Constraint:** For the `lle` function, `alpha` must be `> 0`.
* **LLE Neighborhood Definition:** For each data point `xi`, define its local neighborhood by finding its `k` nearest neighbors.
* **LLE Distance Prerequisite:** As a prerequisite for LLE, calculate distances between all pairs of points.
* **LLE Nearest Neighbor Selection:** For nearest neighbor selection in LLE, find the `k` smallest entries in each row of the distance matrix.
* **`find.kNNs` Logic 1:** To obtain `k` neighbors using `find.kNNs`, identify the `k + 1` closest points from calculated distances.
* **`find.kNNs` Logic 2:** In `find.kNNs`, discard the first column from `smallest.by.rows` output (corresponds to the point itself).
* **`smallest.by.rows` `k` Constraint:** For `smallest.by.rows`, `k` must be less than or equal to `ncol(m)`.
* **LLE Weight Minimization Objective:** For LLE, minimize the Residual Sum of Squares (RSS) for reconstructing each `xi` from its neighbors.
* **LLE Neighbor-Weight Constraint:** For LLE weights, set `wij = 0` unless `xj` is one of `xi`'s `k`-nearest neighbors.
* **LLE Weight Sum Constraint:** For each point `i` in LLE, ensure the sum of its reconstruction weights `sum(wij for j)` equals 1.
* **LLE Weight Centering:** For LLE weight calculation, center neighbor vectors by `yj_tilde = yj - xi`.
* **LLE Weight Minimization Problem:** The LLE weight minimization problem is `min(w_i^T G_i w_i)`, where `G_i` is the Gram matrix `zi zi^T`.
* **LLE Lagrange Multipliers:** Use Lagrange multipliers to enforce the `sum(wij for j) = 1` constraint in LLE weight minimization.
* **LLE Invertible Gram Matrix Solution:** If the LLE Gram matrix `G_i` is invertible, `w_i = (lambda/2) * G_i^-1 * 1`.
* **LLE Lagrange Multiplier Adjustment:** Adjust `lambda` to ensure `sum(wij for j) = 1` in LLE weight calculation.
* **LLE Regularization Condition:** Apply L2 (Tikhonov) regularization if `k > p` in LLE weight calculation.
* **LLE Regularization Parameter Usage:** When applying L2 regularization in LLE, typically set `alpha` to a small but non-zero value.
* **LLE Regularized Objective:** If `k > p` in LLE, the regularized weight minimization objective is `w_i^T G_i w_i + alpha * w_i^T w_i`.
* **LLE Regularized Solution:** If `k > p` in LLE, the regularized weight solution is `w_i = (lambda/2) * (G_i + alpha * I)^-1 * 1`.
* **LLE Weight Matrix Structure:** Each row of the final LLE weight matrix `w` must have `k` non-zero entries.
* **LLE Weight Sum Verification:** The absolute difference `abs(rowSums(w) - 1)` must be less than a specified small tolerance (e.g., `1e-07`).
* **LLE Coordinate Objective:** Minimize `E(Y) = Y^T M Y` to find LLE coordinates, where `M = (I - w)^T (I - w)`.
* **LLE Coordinate Mean Constraint:** For LLE coordinates, impose the mean constraint `(1/n) * sum(yi for i) = 0`.
* **LLE Coordinate Covariance Constraint:** For LLE coordinates, impose the covariance constraint `(1/n) * Y^T Y = I`.
* **LLE Coordinate Solution Type:** The LLE coordinate solution `Y` must be an eigenvector of `M`.
* **LLE Coordinate Selection (`g=1`):** For `g=1` LLE coordinates, take the two bottom eigenfunctions of `M` and discard the constant eigenfunction (eigenvalue 0).
* **LLE Coordinate Selection (`g>1`):** To obtain `g > 1` LLE coordinates, take the `g+1` bottom eigenfunctions of `M`, discard the constant eigenfunction (eigenvalue 0), and use the remaining `g` eigenfunctions as coordinates.
* **`reconstruction.weights` `x`:** For `reconstruction.weights`, input `x` must be a matrix.
* **`reconstruction.weights` `neighbors`:** For `reconstruction.weights`, input `neighbors` must be a matrix and `nrow(neighbors)` must equal `nrow(x)`.
* **`local.weights` `focal`:** For `local.weights`, `focal` must have 1 row, and `ncol(focal)` must equal `ncol(neighbors)`.
* **`local.weights` Regularization Logic:** In `local.weights`, if `solve(gram, rep(1, k))` fails, use the regularized solution `solve(gram + alpha * diag(k), rep(1, k))`.
* **`local.weights` Normalization:** `local.weights` must normalize calculated weights by dividing them by their sum.
* **`local.weights.for.index` Constraints:** For `local.weights.for.index`, `n` must be `> 0`, `focal` must be `> 0` and `<= n`, and `nrow(NNs)` must equal `n`.
* **`coords.from.weights` `w` Matrix:** For `coords.from.weights`, `w` must be a square matrix (`ncol(w) == n`).
* **`coords.from.weights` `w` Row Sums:** For `coords.from.weights`, all row sums of `w` must be within a specified tolerance of 1.
* **`coords.from.weights` `M` Calculation:** For `coords.from.weights`, calculate `M = t(diag(n) - w) %*% (diag(n) - w)`.
* **`coords.from.weights` Eigenvector Calculation:** For `coords.from.weights`, obtain the eigenvectors of `M`.
* **`coords.from.weights` Coordinate Selection:** For `coords.from.weights`, select coordinates from eigenvectors using the range `((n - q):(n - 1))`.

## 10. Density Estimation

* **Histogram Density:** Histogram probability density is estimated as uniform within each bin, resulting in a piecewise-constant estimate.
* **Histogram Consistency:** Histogram density estimates are consistent when bin width `h -> 0` but `n*h -> infinity` as `n -> infinity`.
* **Histogram Optimal Bin Width:** Optimal histogram bin width `h_opt = O(n^(-1/3))` for minimizing Integrated Squared Error (ISE).
* **Kernel Density Estimate Formula:** The Kernel Density Estimate is `f_hat(x) = (1/n) * sum( (1/h) * K((x-x_i)/h) )`.
* **Kernel `1/h` Factor:** The `1/h` factor in the kernel sum ensures `f_hat` integrates to 1.
* **Kernel Density Consistency:** For kernel density estimation consistency, bandwidth `h` must go to zero, but slower than `1/n`.
* **Kernel Optimal Bandwidth:** Optimal kernel bandwidth `h_opt = O(n^(-1/5))` for minimizing ISE.
* **Multivariate Kernel Density Estimate:** The Multivariate Kernel Density Estimate is `f_hat(x) = (1/n) * sum(K(x-x_i)/h)`, where `K` is a multivariate kernel.
* **Product Kernel:** Multivariate kernel density estimation often uses a product of one-dimensional kernels, requiring a bandwidth for each coordinate.
* **Multivariate Kernel Optimal ISE Rate:** Multivariate kernel optimal ISE rate is `O(n^(-4/(p+4)))` in `p` dimensions.
* **Categorical Kernel (Unordered):** For unordered categorical variables, use a kernel `K(x_j, x_i) = 1-h` if `x_j=x_i`, `h/(c-1)` if `x_j!=x_i` (for `c` values, `0 < h < 1`).
* **Conditional Density:** Conditional density is defined as `f(y|x) = f(x,y) / f(x)`.
* **Relative Distribution PDF:** The Relative Distribution PDF is `g(y) = f(Q_0(y)) / f_0(Q_0(y))` for `y in [0,1]`.
* **Relative Distribution Invariance:** The relative distribution is invariant under monotonic transformations of the variable.
* **Density Bandwidth CV:** Use cross-validation to pick bandwidths for density estimation, as it attains near-optimal rates.
* **Plug-in Method (Bandwidth):** The Plug-in method can refine density estimation bandwidth selection by iteratively estimating density and recalculating optimal bandwidth.
* **Curse of Dimensionality (Density):** High-dimensional distributions are hard to learn in density estimation; special assumptions are needed.
* **KDE Likelihood Maximization:** Maximizing in-sample likelihood for Kernel Density Estimation (KDE) leads to infinitesimally small bandwidths; use cross-validated log-likelihood for bandwidth selection instead.
* **Smooth Test Alternative PDF (Uniform):** For Smooth Tests, an alternative PDF (uniform) is `g(y; theta) = exp(sum(theta_j * h_j(y))) / Z(theta)` for `0 <= y <= 1`.
* **Smooth Test Null Hypothesis (Uniform):** For Smooth Tests, `theta = 0` implies uniform density under the null hypothesis.
* **Smooth Test Alternative PDF (Non-uniform):** For Smooth Tests, an alternative PDF (non-uniform) is `g_X(x; theta) = g(F(x); theta) * f(x)`.
* **Smooth Test Data Constraints:** For Smooth Tests for Continuous Distributions, `X` must have a continuous PDF `f`, and CDF `F` must be continuous and strictly increasing on its support.
* **Smooth Test Basis Functions:** Smooth Test basis functions `h_j` must be orthonormal: orthogonal to each other and a constant, and normalized (`Integral from 0 to 1 of h_j(y) dy = 0`; `Integral from 0 to 1 of h_j(y) * h_k(y) dy = 0` for `j != k`; `Integral from 0 to 1 of h_j(y)^2 dy = 1`).

## 11. Reporting & Documentation

* **Text Layout:** Lay out report text cleanly with clear divisions and transitions between sections and sub-sections.
* **Writing Quality:** Ensure writing is well-organized, free of grammatical/mechanical errors, uses complete sentences, is logically grouped, and easy to follow from the presumed level of knowledge.
* **Numerical Precision & Uncertainty:** Report numerical results and summaries to suitable precision, including appropriate measures of uncertainty.
* **Figures & Tables:** Figures and tables must be easy to read, have informative captions, include axis labels and legends, and be placed near corresponding text.
* **Sentence-based Answers:** Answer all problem parts with coherent sentences; do not use raw code or its output as direct answers.
* **Report Length:** The main report must be at most 10 single-spaced pages, including figures.
* **`INTRODUCTION` Section:** The report must contain an `INTRODUCTION` section describing the scientific problem and data set, avoiding Exploratory Data Analysis (EDA) solely for its presence.
* **`MODELS` Section:** The report must contain a `MODELS` section with subsections describing model specification(s), choices, estimated coefficients/functions with uncertainty, and a goodness-of-fit check (procedures, rationale, results, interpretation).
* **`RESULTS` Section:** The report must contain a `RESULTS` section that answers analytical questions quantitatively with uncertainty measures, referencing estimated model(s).
* **Audience Assumption:** Assume general familiarity with course models/methods, but remind readers of specific details. Do not assume prior familiarity with the data set.
* **Code Blocks in Report:** The main report text must be free of intrusive code blocks; use code blocks only for specific computational points or clearest explanations.
* **Regression Coefficient Reporting:** Report all regression coefficients and standard errors to reasonable precision; do not directly paste R’s output.
* **`ID` Variable Exclusion Explanation:** Explain why the `ID` variable must be excluded from regression.
* **Variable Exclusion/Inclusion Justification:** Explain which other variables were excluded (if any) and why, or justify their inclusion.
* **R-squared Reporting:** Report the R-squared and adjusted R-squared of models being compared.
* **5-fold CV Difficulty Explanation:** Explain why using 5-fold cross-validation would be difficult in the context of `A.2 problem 3c`.
* **Kernel Regression Coefficient Reporting:** Report kernel regression coefficients or explain why they cannot be given.
* **`npreg` MSE Reporting:** Report `npreg`'s cross-validated estimate of Mean Squared Error (MSE) for the fitted model.
* **GDP/Undervaluation Interaction:** Determine and explain if there is evidence of interaction between initial GDP and undervaluation.
* **Linear Model APC Calculation:** Explain how to calculate average predictive comparisons from linear model coefficients, and provide values for initial log GDP and undervaluation.
* **Kernel vs. Linear APC Comparison:** Qualitatively compare average effects of increasing initial GDP and undervaluation on growth between kernel and linear regression.
* **In-sample MSE Explanation:** Explain why in-sample MSE is an unbiased estimate of generalization error for the `returns = 1/MAPE` model.
* **Linear Regression Coefficient Reporting:** Report coefficient(s) and standard error(s) for linear regressions and state significance.
* **`npreg` Bandwidth/MSE Reporting:** Report the bandwidth and cross-validated MSE from `npreg`.
* **Kernel Regression vs. Parametric Model:** State whether the 90% confidence band for kernel regression includes the best-fitting parametric model line, and interpret its implication for the parametric model.
* **Mobility Standard Error Summary:** Report summary statistics of standard errors for mobility.
* **Mobility Weights Explanation:** Explain why, for modeling mobility, weights should be inverse square standard errors.
* **`se.prop` Implementation:** Explain whether `se.prop` code implements Eq. 1 or Eq. 2.
* **Log Mass Regression Interpretation:** Explain interpretation of slope and intercept from log new mass on log ancestral mass regression, considering transformations.
* **Logistic Regression Coefficient Reporting:** Report logistic regression coefficients, standard errors, R's p-values, and identify 5% significant variables.
* **Logistic Regression Probability Changes:** Explain why changes in predicted probabilities are not equal for the logistic regression model (A.6 problem 2c).
* **GAM `year` Interpretation:** Explain interpretation of estimated effects for `year` in the GAM.
* **Uncertainty Procedure Justification:** Explain why the chosen uncertainty assessment procedure (bootstrap/simulation) is suitable.
* **Model Comparison Justification:** Explain the reasoning behind choices for model comparison procedures (bootstrap/cross-validation).
* **Model Checking Justification:** Describe the model checking procedure and explain its appropriateness.

## 12. Visualization & Plotting

* **Mobility Maps:** For mobility maps, use longitude (x) and latitude (y). Indicate mobility by color (possibly grayscale) or another suitable device. Maps must be legible.
* **Scatter Plots (Mobility):** Scatter plots must show mobility against specified variables, including a line for simple/univariate regression.
* **Coefficients vs. Time Plot:** Plot coefficients on `year` versus time.
* **Kernel vs. Linear Prediction Plot:** Plot kernel regression predicted values against linear model predicted values.
* **Kernel Residual Plot:** Plot kernel regression residuals against predicted values and assess if they are scattered around a flat line (and if they should be).
* **"More Fun with Stargazing" Plot:** For "More fun with stargazing," only one plot is allowed; explain its parts clearly. "Line" refers to straight or curved lines, as appropriate; disconnected points receive partial credit.
* **Returns vs. `MAPE` Scatterplot:** Plot a scatterplot of returns against `MAPE`.
* **Returns Prediction Lines:** Add prediction lines from problem 2 model, problem 3 model, and `returns = 1/MAPE` model to the plot.
* **Kernel Regression Line:** Add a line of kernel regression predictions to the plot from problem 4.
* **Feature Discovery Plot:** For extra credit (feature discovery), create a color or three-dimensional plot showing predictions as a function of `Price` and `Earnings_10MA_back`.
* **Mobility Standard Error Histogram:** Plot a histogram of standard errors for mobility.
* **Standard Errors vs. Population Plot:** Make a scatterplot of standard errors vs. population for mobility.
* **Standard Errors vs. Mobility Plot:** Make a scatterplot of standard errors vs. mobility.
* **Log Mass Regression Plot (Grams):** Plot the regression line and scatter-plot of data (in grams, not log-grams) for log new mass on log ancestral mass regression.
* **Linear Model and Spline Plot (Grams):** Create a plot showing data points, linear model (problem 1), and spline, with axes in grams (not log-grams).
* **Spline Confidence Bands:** Add 95% confidence bands for the spline curve to the plot.
* **Spline Standard Error Bands:** Add bands at +/- 2 standard errors for the spline curve to the plot.
* **GAM Partial Response Plots:** Provide plots of the partial response functions for the GAM.
* **Calibration Plot:** For A.6 problem 4, create a calibration plot with predicted probability on the horizontal axis and actual frequency on the vertical.

## 13. Bibliography & Referencing

* **Entry Order:** Arrange bibliography entries alphabetically by the last name of the primary author.
* **Repeated Authors:** For consecutive entries by the exact same author(s), replace the author(s) name(s) with an em dash (—) followed by the year in parentheses.
* **Primary Author Format:** List primary author(s) with last name first, followed by first name initials (e.g., "Lastname, Firstname Initial.").
* **Multiple Authors Format:** Separate multiple authors with commas, using "and" before the final author (e.g., "Lastname, Firstname Initial and Firstname Initial. Lastname").
* **Editors Format:** For edited collections, follow the editor's name(s) with "(eds.)".
* **Publication Year Format:** Enclose publication year in parentheses immediately after author(s) or em dash (e.g., "(1993)").
* **Original/Translated Year:** For translated works, provide both original and translated publication years (e.g., "(1989/1995)").
* **Article Titles Format:** Enclose article titles in double quotation marks (e.g., "“Title of Article.”").
* **Journal/Book/Conference Titles Format:** Format journal, book, and conference titles in italics (e.g., *Journal of Financial Economics*, *Nonlinear Time Series*).
* **Journal Page Range Format:** For journal articles, specify volume number followed by a colon and the page range (e.g., "33: 3-56").
* **Book Publisher Information:** For books, provide city, state/country, and publisher (e.g., "Berlin: Springer-Verlag.").
* **Conference Proceedings Format:** For papers in conference proceedings, use "In" followed by the conference name, editor(s) with "(eds.)", and the page range prefixed by "pp." (e.g., "In Sixteenth International Conference on Artificial Intelligence and Statistics [AISTATS 2013] (Carlos M. Carvalho and Pradeep Ravikumar, eds.), pp. 256-264.").
* **Editions Format:** Append edition numbers as ", Xth edn." (e.g., ", 2nd edn.").
* **URLs Format:** Include the full URL, prefixed by "URL" (e.g., "URL <http://jmlr.org/proceedings/papers/v31/entneri3a.html>").
* **DOIs Format:** Include the DOI, prefixed by "doi:" (e.g., "doi:10.1016/0304-405X(93)90023-5").
* **ISBNs Format:** Include the ISBN, prefixed by "ISBN" (e.g., "ISBN 3-900051-07-0").
* **R Package Name Format:** List R package name, followed by its purpose (e.g., "faraway: Functions and datasets for books by Julian Faaway.").
* **R Package Version Format:** Include the R package version, prefixed by "R package version" (e.g., "R package version 1.0.6.").

## 14. Specific Model Parameters & Constraints

* **`npreg` Tolerances (Specific):** When using `npreg` for specific problems, set `tol` to approximately 10 and `ftol` to approximately 10^-4.
* **Mobility Optimization Initial Guess:** For problem A.4.7 optimization, the initial guess for Confederate mobility must be 0.01, and for non-Confederate, 0.15.
* **Evolution Model Parameters:** Unless specified otherwise (in A.5), use the following model parameters: `sigma_sq = 0.63`, `xmin = 1.8` grams, `xmax = 10^9` grams, `p = 0.025`, and `beta = 1/5000`.
* **Logistic Regression (A.6.1) Variables:** For A.6.1 logistic regression, exclude `country` and `year`, and include a quadratic term for `exports`.
* **Logistic Regression (A.6.2) Reference:** All parts of A.6.2 must refer to the logistic regression model fit in A.6.1.
* **GAM (A.6.5) Exports:** For A.6.5 GAM, an explicit quadratic term for `exports` must *not* be included.
* **Kernel Functions:** Kernel functions `K(x_i, x)` must satisfy: (1) `K(x_i, x) >= 0`, (2) depends only on `|x_i - x|`, (3) `integral x K(0, x) dx = 0`, (4) `0 < integral x^2 K(0, x) dx < infinity`.
* **Kernel Regression Zero Weight:** In kernel regression, if `K(x_i, x)` is zero for some `x_i`, those points receive zero weight.
* **Kernel Regression Remote Prediction:** In kernel regression, if all `K(x_i, x)` are zero (e.g., prediction point `x` far from training data), adopt a convention such as returning the global unweighted mean, interpolating, or returning `NA`.
* **Kernel Regression Consistency:** For kernel regression consistency, bandwidth `h` must go to 0 as `n -> infinity`, but `nh -> infinity`.
* **k-Nearest Neighbors Consistency:** For k-nearest neighbors regression consistency, `k` must grow with `n` (e.g., `k -> infinity` and `k/n -> 0` as `n -> infinity`).
* **Smoothing Spline Lambda=Infinity:** For smoothing splines, if `lambda` is set to infinity, the solution must be Ordinary Least Squares (OLS) linear regression.
* **Smoothing Spline Range:** For smoothing splines, the function must be linear outside the range of the data points (`x_1` to `x_n`).

## 15. Copyright & Distribution

* **Document Distribution:** Do not distribute this document without explicit permission.

## Key Highlights

* Follow a scientific approach: posit a model, use it, then check if it matches the data or has flaws.
* For Principal Component Analysis (PCA), data must be centered (each variable has mean 0) and scaled to unit variance when variables have different, incomparable scales.
* Always ensure models are identifiable to obtain meaningful and unique parameter estimates.
* Inferential statistics (p-values, confidence sets) become invalid if the same data is used for both model selection and inference; use an independent data set for valid inference after model selection.
* Do not interpret statistical significance as scientific or real-world significance.
* Do not use regression thoughtlessly for causal inference; it is primarily for probabilistic prediction.
* When evaluating predictions, minimize the expected error (risk or generalization error) on new data, and do not use validation data in model estimation when seeking an unbiased estimate of generalization error.
* Always check the validity of a model's assumptions.
* Cross-entropy is a better metric than misclassification rate for comparing models, as it minimizes the difference between model-predicted and true probabilities.
* For model comparisons of predictive accuracy, do not use R’s default significance tests or R-squared; instead, use suitable bootstrap or cross-validation procedures.

## Example ideas

* Develop and implement automated linters or pre-commit hooks to enforce key coding standards, data preprocessing rules (e.g., centering, scaling, `factor()` usage), and R package-specific constraints outlined in the document.
* Prioritize and categorize all technical rules based on their criticality, impact on model validity, reproducibility, and ethical implications, establishing clear compliance levels for different rule tiers.
* Create a centralized, easily searchable, and interactive knowledge base or checklist from this unified master list to enable data scientists to quickly reference specific rules and requirements during project execution.
* Design and deliver targeted training modules or workshops focusing on the critical aspects of statistical inference cautions, valid model assessment, and rigorous assumption checking, supported by practical examples and case studies.
