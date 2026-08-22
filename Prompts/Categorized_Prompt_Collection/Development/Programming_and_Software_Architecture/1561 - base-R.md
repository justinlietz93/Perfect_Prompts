---
name: base-r
description: Provides base R programming guidance covering data structures, data wrangling, statistical modeling, visualization, and I/O, using only packages included in a standard R installation
---

# Base R Programming Skill

A comprehensive reference for base R programming — covering data structures, control flow, functions, I/O, statistical computing, and plotting.

## Quick Reference

### Data Structures

```r
# Vectors (atomic)
x <- c(1, 2, 3)              # numeric
y <- c("a", "b", "c")        # character
z <- c(TRUE, FALSE, TRUE)    # logical

# Factor
f <- factor(c("low", "med", "high"), levels = c("low", "med", "high"), ordered = TRUE)

# Matrix
m <- matrix(1:6, nrow = 2, ncol = 3)
m[1, ]       # first row
m[, 2]       # second column

# List
lst <- list(name = "ali", scores = c(90, 85), passed = TRUE)
lst$name      # access by name
lst[[2]]      # access by position

# Data frame
df <- data.frame(
  id = 1:3,
  name = c("a", "b", "c"),
  value = c(10.5, 20.3, 30.1),
  stringsAsFactors = FALSE
)
df[df$value > 15, ]    # filter rows
df$new_col <- df$value * 2  # add column
```

### Subsetting

```r
# Vectors
x[1:3]             # by position
x[c(TRUE, FALSE)]  # by logical
x[x > 5]           # by condition
x[-1]              # exclude first

# Data frames
df[1:5, ]                    # first 5 rows
df[, c("name", "value")]     # select columns
df[df$value > 10, "name"]    # filter + select
subset(df, value > 10, select = c(name, value))

# which() for index positions
idx <- which(df$value == max(df$value))
```

### Control Flow

```r
# if/else
if (x > 0) {
  "positive"
} else if (x == 0) {
  "zero"
} else {
  "negative"
}

# ifelse (vectorized)
ifelse(x > 0, "pos", "neg")

# for loop
for (i in seq_along(x)) {
  cat(i, x[i], "\n")
}

# while
while (condition) {
  # body
  if (stop_cond) break
}

# switch
switch(type,
  "a" = do_a(),
  "b" = do_b(),
  stop("Unknown type")
)
```

### Functions

```r
# Define
my_func <- function(x, y = 1, ...) {
  result <- x + y
  return(result)  # or just: result
}

# Anonymous functions
sapply(1:5, function(x) x^2)
# R 4.1+ shorthand:
sapply(1:5, \(x) x^2)

# Useful: do.call for calling with a list of args
do.call(paste, list("a", "b", sep = "-"))
```

### Apply Family

```r
# sapply — simplify result to vector/matrix
sapply(lst, length)

# lapply — always returns list
lapply(lst, function(x) x[1])

# vapply — like sapply but with type safety
vapply(lst, length, integer(1))

# apply — over matrix margins (1=rows, 2=cols)
apply(m, 2, sum)

# tapply — apply by groups
tapply(df$value, df$group, mean)

# mapply — multivariate
mapply(function(x, y) x + y, 1:3, 4:6)

# aggregate — like tapply for data frames
aggregate(value ~ group, data = df, FUN = mean)
```

### String Operations

```r
paste("a", "b", sep = "-")    # "a-b"
paste0("x", 1:3)              # "x1" "x2" "x3"
sprintf("%.2f%%", 3.14159)    # "3.14%"
nchar("hello")                # 5
substr("hello", 1, 3)         # "hel"
gsub("old", "new", text)      # replace all
grep("pattern", x)            # indices of matches
grepl("pattern", x)           # logical vector
strsplit("a,b,c", ",")        # list("a","b","c")
trimws("  hi  ")              # "hi"
tolower("ABC")                # "abc"
```

### Data I/O

```r
# CSV
df <- read.csv("data.csv", stringsAsFactors = FALSE)
write.csv(df, "output.csv", row.names = FALSE)

# Tab-delimited
df <- read.delim("data.tsv")

# General
df <- read.table("data.txt", header = TRUE, sep = "\t")

# RDS (single R object, preserves types)
saveRDS(obj, "data.rds")
obj <- readRDS("data.rds")

# RData (multiple objects)
save(df1, df2, file = "data.RData")
load("data.RData")

# Connections
con <- file("big.csv", "r")
chunk <- readLines(con, n = 100)
close(con)
```

### Base Plotting

```r
# Scatter
plot(x, y, main = "Title", xlab = "X", ylab = "Y",
     pch = 19, col = "steelblue", cex = 1.2)

# Line
plot(x, y, type = "l", lwd = 2, col = "red")
lines(x, y2, col = "blue", lty = 2)  # add line

# Bar
barplot(table(df$category), main = "Counts",
        col = "lightblue", las = 2)

# Histogram
hist(x, breaks = 30, col = "grey80",
     main = "Distribution", xlab = "Value")

# Box plot
boxplot(value ~ group, data = df,
        col = "lightyellow", main = "By Group")

# Multiple plots
par(mfrow = c(2, 2))  # 2x2 grid
# ... four plots ...
par(mfrow = c(1, 1))  # reset

# Save to file
png("plot.png", width = 800, height = 600)
plot(x, y)
dev.off()

# Add elements
legend("topright", legend = c("A", "B"),
       col = c("red", "blue"), lty = 1)
abline(h = 0, lty = 2, col = "grey")
text(x, y, labels = names, pos = 3, cex = 0.8)
```

### Statistics

```r
# Descriptive
mean(x); median(x); sd(x); var(x)
quantile(x, probs = c(0.25, 0.5, 0.75))
summary(df)
cor(x, y)
table(df$category)  # frequency table

# Linear model
fit <- lm(y ~ x1 + x2, data = df)
summary(fit)
coef(fit)
predict(fit, newdata = new_df)
confint(fit)

# t-test
t.test(x, y)                    # two-sample
t.test(x, mu = 0)               # one-sample
t.test(before, after, paired = TRUE)

# Chi-square
chisq.test(table(df$a, df$b))

# ANOVA
fit <- aov(value ~ group, data = df)
summary(fit)
TukeyHSD(fit)

# Correlation test
cor.test(x, y, method = "pearson")
```

### Data Manipulation

```r
# Merge (join)
merged <- merge(df1, df2, by = "id")                  # inner
merged <- merge(df1, df2, by = "id", all = TRUE)      # full outer
merged <- merge(df1, df2, by = "id", all.x = TRUE)    # left

# Reshape
wide <- reshape(long, direction = "wide",
                idvar = "id", timevar = "time", v.names = "value")
long <- reshape(wide, direction = "long",
                varying = list(c("v1", "v2")), v.names = "value")

# Sort
df[order(df$value), ]              # ascending
df[order(-df$value), ]             # descending
df[order(df$group, -df$value), ]   # multi-column

# Remove duplicates
df[!duplicated(df), ]
df[!duplicated(df$id), ]

# Stack / combine
rbind(df1, df2)    # stack rows (same columns)
cbind(df1, df2)    # bind columns (same rows)

# Transform columns
df$log_val <- log(df$value)
df$category <- cut(df$value, breaks = c(0, 10, 20, Inf),
                   labels = c("low", "med", "high"))
```

### Environment & Debugging

```r
ls()                  # list objects
rm(x)                 # remove object
rm(list = ls())       # clear all
str(obj)              # structure
class(obj)            # class
typeof(obj)           # internal type
is.na(x)              # check NA
complete.cases(df)    # rows without NA
traceback()           # after error
debug(my_func)        # step through
browser()             # breakpoint in code
system.time(expr)     # timing
Sys.time()            # current time
```

## Reference Files

For deeper coverage, read the reference files in `references/`:

### Function Gotchas & Quick Reference (condensed from R 4.5.3 Reference Manual)
Non-obvious behaviors, surprising defaults, and tricky interactions — only what Claude doesn't already know:
- **data-wrangling.md** — Read when: subsetting returns wrong type, apply on data frame gives unexpected coercion, merge/split/cbind behaves oddly, factor levels persist after filtering, table/duplicated edge cases.
- **modeling.md** — Read when: formula syntax is confusing (`I()`, `*` vs `:`, `/`), aov gives wrong SS type, glm silently fits OLS, nls won't converge, predict returns wrong scale, optim/optimize needs tuning.
- **statistics.md** — Read when: hypothesis test gives surprising result, need to choose correct p.adjust method, clustering parameters seem wrong, distribution function naming is confusing (`d`/`p`/`q`/`r` prefixes).
- **visualization.md** — Read when: par settings reset unexpectedly, layout/mfrow interaction is confusing, axis labels are clipped, colors don't look right, need specialty plots (contour, persp, mosaic, pairs).
- **io-and-text.md** — Read when: read.table silently drops data or misparses columns, regex behaves differently than expected, sprintf formatting is tricky, write.table output has unwanted row names.
- **dates-and-system.md** — Read when: Date/POSIXct conversion gives wrong day, time zones cause off-by-one, difftime units are unexpected, need to find/list/test files programmatically.
- **misc-utilities.md** — Read when: do.call behaves differently than direct call, need Reduce/Filter/Map, tryCatch handler doesn't fire, all.equal returns string not logical, time series functions need setup.

## Tips for Writing Good R Code

- Use `vapply()` over `sapply()` in production code — it enforces return types
- Prefer `seq_along(x)` over `1:length(x)` — the latter breaks when `x` is empty
- Use `stringsAsFactors = FALSE` in `read.csv()` / `data.frame()` (default changed in R 4.0)
- Vectorize operations instead of writing loops when possible
- Use `stop()`, `warning()`, `message()` for error handling — not `print()`
- `<<-` assigns to parent environment — use sparingly and intentionally
- `with(df, expr)` avoids repeating `df$` everywhere
- `Sys.setenv()` and `.Renviron` for environment variables
FILE:references/misc-utilities.md
# Miscellaneous Utilities — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## do.call

- `do.call(fun, args_list)` — `args` must be a **list**, even for a single argument.
- `quote = TRUE` prevents evaluation of arguments before the call — needed when passing expressions/symbols.
- Behavior of `substitute` inside `do.call` differs from direct calls. Semantics are not fully defined for this case.
- Useful pattern: `do.call(rbind, list_of_dfs)` to combine a list of data frames.

---

## Reduce / Filter / Map / Find / Position

R's functional programming helpers from base — genuinely non-obvious.

- `Reduce(f, x)` applies binary function `f` cumulatively: `Reduce("+", 1:4)` = `((1+2)+3)+4`. Direction matters for non-commutative ops.
- `Reduce(f, x, accumulate = TRUE)` returns all intermediate results — equivalent to Python's `itertools.accumulate`.
- `Reduce(f, x, right = TRUE)` folds from the right: `f(x1, f(x2, f(x3, x4)))`.
- `Reduce` with `init` adds a starting value: `Reduce(f, x, init = v)` = `f(f(f(v, x1), x2), x3)`.
- `Filter(f, x)` keeps elements where `f(elem)` is `TRUE`. Unlike `x[sapply(x, f)]`, handles `NULL`/empty correctly.
- `Map(f, ...)` is a simple wrapper for `mapply(f, ..., SIMPLIFY = FALSE)` — always returns a list.
- `Find(f, x)` returns the **first** element where `f(elem)` is `TRUE`. `Find(f, x, right = TRUE)` for last.
- `Position(f, x)` returns the **index** of the first match (like `Find` but returns position, not value).

---

## lengths

- `lengths(x)` returns the length of **each element** of a list. Equivalent to `sapply(x, length)` but faster (implemented in C).
- Works on any list-like object. Returns integer vector.

---

## conditions (tryCatch / withCallingHandlers)

- `tryCatch` **unwinds** the call stack — handler runs in the calling environment, not where the error occurred. Cannot resume execution.
- `withCallingHandlers` does NOT unwind — handler runs where the condition was signaled. Can inspect/log then let the condition propagate.
- `tryCatch(expr, error = function(e) e)` returns the error condition object.
- `tryCatch(expr, warning = function(w) {...})` catches the **first** warning and exits. Use `withCallingHandlers` + `invokeRestart("muffleWarning")` to suppress warnings but continue.
- `tryCatch` `finally` clause always runs (like Java try/finally).
- `globalCallingHandlers()` registers handlers that persist for the session (useful for logging).
- Custom conditions: `stop(errorCondition("msg", class = "myError"))` then catch with `tryCatch(..., myError = function(e) ...)`.

---

## all.equal

- Tests **near equality** with tolerance (default `1.5e-8`, i.e., `sqrt(.Machine$double.eps)`).
- Returns `TRUE` or a **character string** describing the difference — NOT `FALSE`. Use `isTRUE(all.equal(x, y))` in conditionals.
- `tolerance` argument controls numeric tolerance. `scale` for absolute vs relative comparison.
- Checks attributes, names, dimensions — more thorough than `==`.

---

## combn

- `combn(n, m)` or `combn(x, m)`: generates all combinations of `m` items from `x`.
- Returns a **matrix** with `m` rows; each column is one combination.
- `FUN` argument applies a function to each combination: `combn(5, 3, sum)` returns sums of all 3-element subsets.
- `simplify = FALSE` returns a list instead of a matrix.

---

## modifyList

- `modifyList(x, val)` replaces elements of list `x` with those in `val` by **name**.
- Setting a value to `NULL` **removes** that element from the list.
- **Does** add new names not in `x` — it uses `x[names(val)] <- val` internally, so any name in `val` gets added or replaced.

---

## relist

- Inverse of `unlist`: given a flat vector and a skeleton list, reconstructs the nested structure.
- `relist(flesh, skeleton)` — `flesh` is the flat data, `skeleton` provides the shape.
- Works with factors, matrices, and nested lists.

---

## txtProgressBar

- `txtProgressBar(min, max, style = 3)` — style 3 shows percentage + bar (most useful).
- Update with `setTxtProgressBar(pb, value)`. Close with `close(pb)`.
- Style 1: rotating `|/-\`, style 2: simple progress. Only style 3 shows percentage.

---

## object.size

- Returns an **estimate** of memory used by an object. Not always exact for shared references.
- `format(object.size(x), units = "MB")` for human-readable output.
- Does not count the size of environments or external pointers.

---

## installed.packages / update.packages

- `installed.packages()` can be slow (scans all packages). Use `find.package()` or `requireNamespace()` to check for a specific package.
- `update.packages(ask = FALSE)` updates all packages without prompting.
- `lib.loc` specifies which library to check/update.

---

## vignette / demo

- `vignette()` lists all vignettes; `vignette("name", package = "pkg")` opens a specific one.
- `demo()` lists all demos; `demo("topic")` runs one interactively.
- `browseVignettes()` opens vignette browser in HTML.

---

## Time series: acf / arima / ts / stl / decompose

- `ts(data, start, frequency)`: `frequency` is observations per unit time (12 for monthly, 4 for quarterly).
- `acf` default `type = "correlation"`. Use `type = "partial"` for PACF. `plot = FALSE` to suppress auto-plotting.
- `arima(x, order = c(p,d,q))` for ARIMA models. `seasonal = list(order = c(P,D,Q), period = S)` for seasonal component.
- `arima` handles `NA` values in the time series (via Kalman filter).
- `stl` requires `s.window` (seasonal window) — must be specified, no default. `s.window = "periodic"` assumes fixed seasonality.
- `decompose`: simpler than `stl`, uses moving averages. `type = "additive"` or `"multiplicative"`.
- `stl` result components: `$time.series` matrix with columns `seasonal`, `trend`, `remainder`.
FILE:references/data-wrangling.md
# Data Wrangling — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## Extract / Extract.data.frame

Indexing pitfalls in base R.

- `m[j = 2, i = 1]` is `m[2, 1]` not `m[1, 2]` — argument names are **ignored** in `[`, positional matching only. Never name index args.
- Factor indexing: `x[f]` uses integer codes of factor `f`, not its character labels. Use `x[as.character(f)]` for label-based indexing.
- `x[[]]` with no index is always an error. `x$name` does partial matching by default; `x[["name"]]` does not (exact by default).
- Assigning `NULL` via `x[[i]] <- NULL` or `x$name <- NULL` **deletes** that list element.
- Data frame `[` with single column: `df[, 1]` returns a **vector** (drop=TRUE default for columns), but `df[1, ]` returns a **data frame** (drop=FALSE for rows). Use `drop = FALSE` explicitly.
- Matrix indexing a data frame (`df[cbind(i,j)]`) coerces to matrix first — avoid.

---

## subset

Use interactively only; unsafe for programming.

- `subset` argument uses **non-standard evaluation** — column names are resolved in the data frame, which can silently pick up wrong variables in programmatic use. Use `[` with explicit logic in functions.
- `NA`s in the logical condition are treated as `FALSE` (rows silently dropped).
- Factors may retain unused levels after subsetting; call `droplevels()`.

---

## match / %in%

- `%in%` **never returns NA** — this makes it safe for `if()` conditions unlike `==`.
- `match()` returns position of **first** match only; duplicates in `table` are ignored.
- Factors, raw vectors, and lists are all converted to character before matching.
- `NaN` matches `NaN` but not `NA`; `NA` matches `NA` only.

---

## apply

- On a **data frame**, `apply` coerces to matrix via `as.matrix` first — mixed types become character.
- Return value orientation is transposed: if FUN returns length-n vector, result has dim `c(n, dim(X)[MARGIN])`. Row results become **columns**.
- Factor results are coerced to character in the output array.
- `...` args cannot share names with `X`, `MARGIN`, or `FUN` (partial matching risk).

---

## lapply / sapply / vapply

- `sapply` can return a vector, matrix, or list unpredictably — use `vapply` in non-interactive code with explicit `FUN.VALUE` template.
- Calling primitives directly in `lapply` can cause dispatch issues; wrap in `function(x) is.numeric(x)` rather than bare `is.numeric`.
- `sapply` with `simplify = "array"` can produce higher-rank arrays (not just matrices).

---

## tapply

- Returns an **array** (not a data frame). Class info on return values is **discarded** (e.g., Date objects become numeric).
- `...` args to FUN are **not** divided into cells — they apply globally, so FUN should not expect additional args with same length as X.
- `default = NA` fills empty cells; set `default = 0` for sum-like operations. Before R 3.4.0 this was hard-coded to `NA`.
- Use `array2DF()` to convert result to a data frame.

---

## mapply

- Argument name is `SIMPLIFY` (all caps) not `simplify` — inconsistent with `sapply`.
- `MoreArgs` must be a **list** of args not vectorized over.
- Recycles shorter args to common length; zero-length arg gives zero-length result.

---

## merge

- Default `by` is `intersect(names(x), names(y))` — can silently merge on unintended columns if data frames share column names.
- `by = 0` or `by = "row.names"` merges on row names, adding a "Row.names" column.
- `by = NULL` (or both `by.x`/`by.y` length 0) produces **Cartesian product**.
- Result is sorted on `by` columns by default (`sort = TRUE`). For unsorted output use `sort = FALSE`.
- Duplicate key matches produce **all combinations** (one row per match pair).

---

## split

- If `f` is a list of factors, interaction is used; levels containing `"."` can cause unexpected splits unless `sep` is changed.
- `drop = FALSE` (default) retains empty factor levels as empty list elements.
- Supports formula syntax: `split(df, ~ Month)`.

---

## cbind / rbind

- `cbind` on data frames calls `data.frame(...)`, not `cbind.matrix`. Mixing matrices and data frames can give unexpected results.
- `rbind` on data frames matches columns **by name**, not position. Missing columns get `NA`.
- `cbind(NULL)` returns `NULL` (not a matrix). For consistency, `rbind(NULL)` also returns `NULL`.

---

## table

- By default **excludes NA** (`useNA = "no"`). Use `useNA = "ifany"` or `exclude = NULL` to count NAs.
- Setting `exclude` non-empty and non-default implies `useNA = "ifany"`.
- Result is always an **array** (even 1D), class "table". Convert to data frame with `as.data.frame(tbl)`.
- Two kinds of NA (factor-level NA vs actual NA) are treated differently depending on `useNA`/`exclude`.

---

## duplicated / unique

- `duplicated` marks the **second and later** occurrences as TRUE, not the first. Use `fromLast = TRUE` to reverse.
- For data frames, operates on whole rows. For lists, compares recursively.
- `unique` keeps the **first** occurrence of each value.

---

## data.frame (gotchas)

- `stringsAsFactors = FALSE` is the default since R 4.0.0 (was TRUE before).
- Atomic vectors recycle to match longest column, but only if exact multiple. Protect with `I()` to prevent conversion.
- Duplicate column names allowed only with `check.names = FALSE`, but many operations will de-dup them silently.
- Matrix arguments are expanded to multiple columns unless protected by `I()`.

---

## factor (gotchas)

- `as.numeric(f)` returns **integer codes**, not original values. Use `as.numeric(levels(f))[f]` or `as.numeric(as.character(f))`.
- Only `==` and `!=` work between factors; factors must have identical level sets. Ordered factors support `<`, `>`.
- `c()` on factors unions level sets (since R 4.1.0), but earlier versions converted to integer.
- Levels are sorted by default, but sort order is **locale-dependent** at creation time.

---

## aggregate

- Formula interface (`aggregate(y ~ x, data, FUN)`) drops `NA` groups by default.
- The data frame method requires `by` as a **list** (not a vector).
- Returns columns named after the grouping variables, with result column keeping the original name.
- If FUN returns multiple values, result column is a **matrix column** inside the data frame.

---

## complete.cases

- Returns a logical vector: TRUE for rows with **no** NAs across all columns/arguments.
- Works on multiple arguments (e.g., `complete.cases(x, y)` checks both).

---

## order

- Returns a **permutation vector** of indices, not the sorted values. Use `x[order(x)]` to sort.
- Default is ascending; use `-x` for descending numeric, or `decreasing = TRUE`.
- For character sorting, depends on locale. Use `method = "radix"` for locale-independent fast sorting.
- `sort.int()` with `method = "radix"` is much faster for large integer/character vectors.
FILE:references/dates-and-system.md
# Dates and System — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## Dates (Date class)

- `Date` objects are stored as **integer days since 1970-01-01**. Arithmetic works in days.
- `Sys.Date()` returns current date as Date object.
- `seq.Date(from, to, by = "month")` — "month" increments can produce varying-length intervals. Adding 1 month to Jan 31 gives Mar 3 (not Feb 28).
- `diff(dates)` returns a `difftime` object in days.
- `format(date, "%Y")` for year, `"%m"` for month, `"%d"` for day, `"%A"` for weekday name (locale-dependent).
- Years before 1CE may not be handled correctly.
- `length(date_vector) <- n` pads with `NA`s if extended.

---

## DateTimeClasses (POSIXct / POSIXlt)

- `POSIXct`: seconds since 1970-01-01 UTC (compact, a numeric vector).
- `POSIXlt`: list with components `$sec`, `$min`, `$hour`, `$mday`, `$mon` (0-11!), `$year` (since 1900!), `$wday` (0-6, Sunday=0), `$yday` (0-365).
- Converting between POSIXct and Date: `as.Date(posixct_obj)` uses `tz = "UTC"` by default — may give different date than intended if original was in another timezone.
- `Sys.time()` returns POSIXct in current timezone.
- `strptime` returns POSIXlt; `as.POSIXct(strptime(...))` to get POSIXct.
- `difftime` arithmetic: subtracting POSIXct objects gives difftime. Units auto-selected ("secs", "mins", "hours", "days", "weeks").

---

## difftime

- `difftime(time1, time2, units = "auto")` — auto-selects smallest sensible unit.
- Explicit units: `"secs"`, `"mins"`, `"hours"`, `"days"`, `"weeks"`. No "months" or "years" (variable length).
- `as.numeric(diff, units = "hours")` to extract numeric value in specific units.
- `units(diff_obj) <- "hours"` changes the unit in place.

---

## system.time / proc.time

- `system.time(expr)` returns `user`, `system`, and `elapsed` time.
- `gcFirst = TRUE` (default): runs garbage collection before timing for more consistent results.
- `proc.time()` returns cumulative time since R started — take differences for intervals.
- `elapsed` (wall clock) can be less than `user` (multi-threaded BLAS) or more (I/O waits).

---

## Sys.sleep

- `Sys.sleep(seconds)` — allows fractional seconds. Actual sleep may be longer (OS scheduling).
- The process **yields** to the OS during sleep (does not busy-wait).

---

## options (key options)

Selected non-obvious options:

- `options(scipen = n)`: positive biases toward fixed notation, negative toward scientific. Default 0. Applies to `print`/`format`/`cat` but not `sprintf`.
- `options(digits = n)`: significant digits for printing (1-22, default 7). Suggestion only.
- `options(digits.secs = n)`: max decimal digits for seconds in time formatting (0-6, default 0).
- `options(warn = n)`: -1 = ignore warnings, 0 = collect (default), 1 = immediate, 2 = convert to errors.
- `options(error = recover)`: drop into debugger on error. `options(error = NULL)` resets to default.
- `options(OutDec = ",")`: change decimal separator in output (affects `format`, `print`, NOT `sprintf`).
- `options(stringsAsFactors = FALSE)`: global default for `data.frame` (moot since R 4.0.0 where it's already FALSE).
- `options(expressions = 5000)`: max nested evaluations. Increase for deep recursion.
- `options(max.print = 99999)`: controls truncation in `print` output.
- `options(na.action = "na.omit")`: default NA handling in model functions.
- `options(contrasts = c("contr.treatment", "contr.poly"))`: default contrasts for unordered/ordered factors.

---

## file.path / basename / dirname

- `file.path("a", "b", "c.txt")` → `"a/b/c.txt"` (platform-appropriate separator).
- `basename("/a/b/c.txt")` → `"c.txt"`. `dirname("/a/b/c.txt")` → `"/a/b"`.
- `file.path` does NOT normalize paths (no `..` resolution); use `normalizePath()` for that.

---

## list.files

- `list.files(pattern = "*.csv")` — `pattern` is a **regex**, not a glob! Use `glob2rx("*.csv")` or `"\\.csv$"`.
- `full.names = FALSE` (default) returns basenames only. Use `full.names = TRUE` for complete paths.
- `recursive = TRUE` to search subdirectories.
- `all.files = TRUE` to include hidden files (starting with `.`).

---

## file.info

- Returns data frame with `size`, `isdir`, `mode`, `mtime`, `ctime`, `atime`, `uid`, `gid`.
- `mtime`: modification time (POSIXct). Useful for `file.info(f)$mtime`.
- On some filesystems, `ctime` is status-change time, not creation time.

---

## file_test

- `file_test("-f", path)`: TRUE if regular file exists.
- `file_test("-d", path)`: TRUE if directory exists.
- `file_test("-nt", f1, f2)`: TRUE if f1 is newer than f2.
- More reliable than `file.exists()` for distinguishing files from directories.
FILE:references/io-and-text.md
# I/O and Text Processing — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## read.table (gotchas)

- `sep = ""` (default) means **any whitespace** (spaces, tabs, newlines) — not a literal empty string.
- `comment.char = "#"` by default — lines with `#` are truncated. Use `comment.char = ""` to disable (also faster).
- `header` auto-detection: set to TRUE if first row has **one fewer field** than subsequent rows (the missing field is assumed to be row names).
- `colClasses = "NULL"` **skips** that column entirely — very useful for speed.
- `read.csv` defaults differ from `read.table`: `header = TRUE`, `sep = ","`, `fill = TRUE`, `comment.char = ""`.
- For large files: specifying `colClasses` and `nrows` dramatically reduces memory usage. `read.table` is slow for wide data frames (hundreds of columns); use `scan` or `data.table::fread` for matrices.
- `stringsAsFactors = FALSE` since R 4.0.0 (was TRUE before).

---

## write.table (gotchas)

- `row.names = TRUE` by default — produces an unnamed first column that confuses re-reading. Use `row.names = FALSE` or `col.names = NA` for Excel-compatible CSV.
- `write.csv` fixes `sep = ","`, `dec = "."`, and uses `qmethod = "double"` — cannot override these via `...`.
- `quote = TRUE` (default) quotes character/factor columns. Numeric columns are never quoted.
- Matrix-like columns in data frames expand to multiple columns silently.
- Slow for data frames with many columns (hundreds+); each column processed separately by class.

---

## read.fwf

- Reads fixed-width format files. `widths` is a vector of field widths.
- **Negative widths skip** that many characters (useful for ignoring fields).
- `buffersize` controls how many lines are read at a time; increase for large files.
- Uses `read.table` internally after splitting fields.

---

## count.fields

- Counts fields per line in a file — useful for diagnosing read errors.
- `sep` and `quote` arguments match those of `read.table`.

---

## grep / grepl / sub / gsub (gotchas)

- Three regex modes: POSIX extended (default), `perl = TRUE`, `fixed = TRUE`. They behave differently for edge cases.
- **Name arguments explicitly** — unnamed args after `x`/`pattern` are matched positionally to `ignore.case`, `perl`, etc. Common source of silent bugs.
- `sub` replaces **first** match only; `gsub` replaces **all** matches.
- Backreferences: `"\\1"` in replacement (double backslash in R strings). With `perl = TRUE`: `"\\U\\1"` for uppercase conversion.
- `grep(value = TRUE)` returns matching **elements**; `grep(value = FALSE)` (default) returns **indices**.
- `grepl` returns logical vector — preferred for filtering.
- `regexpr` returns first match position + length (as attributes); `gregexpr` returns all matches as a list.
- `regexec` returns match + capture group positions; `gregexec` does this for all matches.
- Character classes like `[:alpha:]` must be inside `[[:alpha:]]` (double brackets) in POSIX mode.

---

## strsplit

- Returns a **list** (one element per input string), even for a single string.
- `split = ""` or `split = character(0)` splits into individual characters.
- Match at beginning of string: first element of result is `""`. Match at end: no trailing `""`.
- `fixed = TRUE` is faster and avoids regex interpretation.
- Common mistake: unnamed arguments silently match `fixed`, `perl`, etc.

---

## substr / substring

- `substr(x, start, stop)`: extracts/replaces substring. 1-indexed, inclusive on both ends.
- `substring(x, first, last)`: same but `last` defaults to `1000000L` (effectively "to end"). Vectorized over `first`/`last`.
- Assignment form: `substr(x, 1, 3) <- "abc"` replaces in place (must be same length replacement).

---

## trimws

- `which = "both"` (default), `"left"`, or `"right"`.
- `whitespace = "[ \\t\\r\\n]"` — customizable regex for what counts as whitespace.

---

## nchar

- `type = "bytes"` counts bytes; `type = "chars"` (default) counts characters; `type = "width"` counts display width.
- `nchar(NA)` returns `NA` (not 2). `nchar(factor)` works on the level labels.
- `keepNA = TRUE` (default since R 3.3.0); set to `FALSE` to count `"NA"` as 2 characters.

---

## format / formatC

- `format(x, digits, nsmall)`: `nsmall` forces minimum decimal places. `big.mark = ","` adds thousands separator.
- `formatC(x, format = "f", digits = 2)`: C-style formatting. `format = "e"` for scientific, `"g"` for general.
- `format` returns character vector; always right-justified by default (`justify = "right"`).

---

## type.convert

- Converts character vectors to appropriate types (logical, integer, double, complex, character).
- `as.is = TRUE` (recommended): keeps characters as character, not factor.
- Applied column-wise on data frames. `tryLogical = TRUE` (R 4.3+) converts "TRUE"/"FALSE" columns.

---

## Rscript

- `commandArgs(trailingOnly = TRUE)` gets script arguments (excluding R/Rscript flags).
- `#!` line on Unix: `/usr/bin/env Rscript` or full path.
- `--vanilla` or `--no-init-file` to skip `.Rprofile` loading.
- Exit code: `quit(status = 1)` for error exit.

---

## capture.output

- Captures output from `cat`, `print`, or any expression that writes to stdout.
- `file = NULL` (default) returns character vector. `file = "out.txt"` writes directly to file.
- `type = "message"` captures stderr instead.

---

## URLencode / URLdecode

- `URLencode(url, reserved = FALSE)` by default does NOT encode reserved chars (`/`, `?`, `&`, etc.).
- Set `reserved = TRUE` to encode a URL **component** (query parameter value).

---

## glob2rx

- Converts shell glob patterns to regex: `glob2rx("*.csv")` → `"^.*\\.csv$"`.
- Useful with `list.files(pattern = glob2rx("data_*.RDS"))`.
FILE:references/modeling.md
# Modeling — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## formula

Symbolic model specification gotchas.

- `I()` is required to use arithmetic operators literally: `y ~ x + I(x^2)`. Without `I()`, `^` means interaction crossing.
- `*` = main effects + interaction: `a*b` expands to `a + b + a:b`.
- `(a+b+c)^2` = all main effects + all 2-way interactions (not squaring).
- `-` removes terms: `(a+b+c)^2 - a:b` drops only the `a:b` interaction.
- `/` means nesting: `a/b` = `a + b %in% a` = `a + a:b`.
- `.` in formula means "all other columns in data" (in `terms.formula` context) or "previous contents" (in `update.formula`).
- Formula objects carry an **environment** used for variable lookup; `as.formula("y ~ x")` uses `parent.frame()`.

---

## terms / model.matrix

- `model.matrix` creates the design matrix including dummy coding. Default contrasts: `contr.treatment` for unordered factors, `contr.poly` for ordered.
- `terms` object attributes: `order` (interaction order per term), `intercept`, `factors` matrix.
- Column names from `model.matrix` can be surprising: e.g., `factorLevelName` concatenation.

---

## glm

- Default `family = gaussian(link = "identity")` — `glm()` with no `family` silently fits OLS (same as `lm`, but slower and with deviance-based output).
- Common families: `binomial(link = "logit")`, `poisson(link = "log")`, `Gamma(link = "inverse")`, `inverse.gaussian()`.
- `binomial` accepts response as: 0/1 vector, logical, factor (second level = success), or 2-column matrix `cbind(success, failure)`.
- `weights` in `glm` means **prior weights** (not frequency weights) — for frequency weights, use the cbind trick or offset.
- `predict.glm(type = "response")` for predicted probabilities; default `type = "link"` returns log-odds (for logistic) or log-rate (for Poisson).
- `anova(glm_obj, test = "Chisq")` for deviance-based tests; `"F"` is invalid for non-Gaussian families.
- Quasi-families (`quasibinomial`, `quasipoisson`) allow overdispersion — no AIC is computed.
- Convergence: `control = glm.control(maxit = 100)` if default 25 iterations isn't enough.

---

## aov

- `aov` is a wrapper around `lm` that stores extra info for balanced ANOVA. For unbalanced designs, Type I SS (sequential) are computed — order of terms matters.
- For Type III SS, use `car::Anova()` or set contrasts to `contr.sum`/`contr.helmert`.
- Error strata for repeated measures: `aov(y ~ A*B + Error(Subject/B))`.
- `summary.aov` gives ANOVA table; `summary.lm(aov_obj)` gives regression-style summary.

---

## nls

- Requires **good starting values** in `start = list(...)` or convergence fails.
- Self-starting models (`SSlogis`, `SSasymp`, etc.) auto-compute starting values.
- Algorithm `"port"` allows bounds on parameters (`lower`/`upper`).
- If data fits too exactly (no residual noise), convergence check fails — use `control = list(scaleOffset = 1)` or jitter data.
- `weights` argument for weighted NLS; `na.action` for missing value handling.

---

## step / add1

- `step` does **stepwise** model selection by AIC (default). Use `k = log(n)` for BIC.
- Direction: `direction = "both"` (default), `"forward"`, or `"backward"`.
- `add1`/`drop1` evaluate single-term additions/deletions; `step` calls these iteratively.
- `scope` argument defines the upper/lower model bounds for search.
- `step` modifies the model object in place — can be slow for large models with many candidate terms.

---

## predict.lm / predict.glm

- `predict.lm` with `interval = "confidence"` gives CI for **mean** response; `interval = "prediction"` gives PI for **new observation** (wider).
- `newdata` must have columns matching the original formula variables — factors must have the same levels.
- `predict.glm` with `type = "response"` gives predictions on the response scale (e.g., probabilities for logistic); `type = "link"` (default) gives on the link scale.
- `se.fit = TRUE` returns standard errors; for `predict.glm` these are on the **link** scale regardless of `type`.
- `predict.lm` with `type = "terms"` returns the contribution of each term.

---

## loess

- `span` controls smoothness (default 0.75). Span < 1 uses that proportion of points; span > 1 uses all points with adjusted distance.
- Maximum **4 predictors**. Memory usage is roughly **quadratic** in n (1000 points ~ 10MB).
- `degree = 0` (local constant) is allowed but poorly tested — use with caution.
- Not identical to S's `loess`; conditioning is not implemented.
- `normalize = TRUE` (default) standardizes predictors to common scale; set `FALSE` for spatial coords.

---

## lowess vs loess

- `lowess` is the older function; returns `list(x, y)` — cannot predict at new points.
- `loess` is the newer formula interface with `predict` method.
- `lowess` parameter is `f` (span, default 2/3); `loess` parameter is `span` (default 0.75).
- `lowess` `iter` default is 3 (robustifying iterations); `loess` default `family = "gaussian"` (no robustness).

---

## smooth.spline

- Default smoothing parameter selected by **GCV** (generalized cross-validation).
- `cv = TRUE` uses ordinary leave-one-out CV instead — do not use with duplicate x values.
- `spar` and `lambda` control smoothness; `df` can specify equivalent degrees of freedom.
- Returns object with `predict`, `print`, `plot` methods. The `fit` component has knots and coefficients.

---

## optim

- **Minimizes** by default. To maximize: set `control = list(fnscale = -1)`.
- Default method is Nelder-Mead (no gradients, robust but slow). Poor for 1D — use `"Brent"` or `optimize()`.
- `"L-BFGS-B"` is the only method supporting box constraints (`lower`/`upper`). Bounds auto-select this method with a warning.
- `"SANN"` (simulated annealing): convergence code is **always 0** — it never "fails". `maxit` = total function evals (default 10000), no other stopping criterion.
- `parscale`: scale parameters so unit change in each produces comparable objective change. Critical for mixed-scale problems.
- `hessian = TRUE`: returns numerical Hessian of the **unconstrained** problem even if box constraints are active.
- `fn` can return `NA`/`Inf` (except `"L-BFGS-B"` which requires finite values always). Initial value must be finite.

---

## optimize / uniroot

- `optimize`: 1D minimization on a bounded interval. Returns `minimum` and `objective`.
- `uniroot`: finds a root of `f` in `[lower, upper]`. **Requires** `f(lower)` and `f(upper)` to have opposite signs.
- `uniroot` with `extendInt = "yes"` can auto-extend the interval to find sign change — but can find spurious roots for functions that don't actually cross zero.
- `nlm`: Newton-type minimizer. Gradient/Hessian as **attributes** of the return value from `fn` (unusual interface).

---

## TukeyHSD

- Requires a fitted `aov` object (not `lm`).
- Default `conf.level = 0.95`. Returns adjusted p-values and confidence intervals for all pairwise comparisons.
- Only meaningful for **balanced** or near-balanced designs; can be liberal for very unbalanced data.

---

## anova (for lm)

- `anova(model)`: sequential (Type I) SS — **order of terms matters**.
- `anova(model1, model2)`: F-test comparing nested models.
- For Type II or III SS use `car::Anova()`.
FILE:references/statistics.md
# Statistics — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## chisq.test

- `correct = TRUE` (default) applies Yates continuity correction for **2x2 tables only**.
- `simulate.p.value = TRUE`: Monte Carlo with `B = 2000` replicates (min p ~ 0.0005). Simulation assumes **fixed marginals** (Fisher-style sampling, not the chi-sq assumption).
- For goodness-of-fit: pass a vector, not a matrix. `p` must sum to 1 (or set `rescale.p = TRUE`).
- Return object includes `$expected`, `$residuals` (Pearson), and `$stdres` (standardized).

---

## wilcox.test

- `exact = TRUE` by default for small samples with no ties. With ties, normal approximation used.
- `correct = TRUE` applies continuity correction to normal approximation.
- `conf.int = TRUE` computes Hodges-Lehmann estimator and confidence interval (not just the p-value).
- Paired test: `paired = TRUE` uses signed-rank test (Wilcoxon), not rank-sum (Mann-Whitney).

---

## fisher.test

- For tables larger than 2x2, uses simulation (`simulate.p.value = TRUE`) or network algorithm.
- `workspace` controls memory for the network algorithm; increase if you get errors on large tables.
- `or` argument tests a specific odds ratio (default 1) — only for 2x2 tables.

---

## ks.test

- Two-sample test or one-sample against a reference distribution.
- Does **not** handle ties well — warns and uses asymptotic approximation.
- For composite hypotheses (parameters estimated from data), p-values are **conservative** (too large). Use `dgof` or `ks.test` with `exact = NULL` for discrete distributions.

---

## p.adjust

- Methods: `"holm"` (default), `"BH"` (Benjamini-Hochberg FDR), `"bonferroni"`, `"BY"`, `"hochberg"`, `"hommel"`, `"fdr"` (alias for BH), `"none"`.
- `n` argument: total number of hypotheses (can be larger than `length(p)` if some p-values are excluded).
- Handles `NA`s: adjusted p-values are `NA` where input is `NA`.

---

## pairwise.t.test / pairwise.wilcox.test

- `p.adjust.method` defaults to `"holm"`. Change to `"BH"` for FDR control.
- `pool.sd = TRUE` (default for t-test): uses pooled SD across all groups (assumes equal variances).
- Returns a matrix of p-values, not test statistics.

---

## shapiro.test

- Sample size must be between 3 and 5000.
- Tests normality; low p-value = evidence against normality.

---

## kmeans

- `nstart > 1` recommended (e.g., `nstart = 25`): runs algorithm from multiple random starts, returns best.
- Default `iter.max = 10` — may be too low for convergence. Increase for large/complex data.
- Default algorithm is "Hartigan-Wong" (generally best). Very close points may cause non-convergence (warning with `ifault = 4`).
- Cluster numbering is arbitrary; ordering may differ across platforms.
- Always returns k clusters when k is specified (except Lloyd-Forgy may return fewer).

---

## hclust

- `method = "ward.D2"` implements Ward's criterion correctly (using squared distances). The older `"ward.D"` did not square distances (retained for back-compatibility).
- Input must be a `dist` object. Use `as.dist()` to convert a symmetric matrix.
- `hang = -1` in `plot()` aligns all labels at the bottom.

---

## dist

- `method = "euclidean"` (default). Other options: `"manhattan"`, `"maximum"`, `"canberra"`, `"binary"`, `"minkowski"`.
- Returns a `dist` object (lower triangle only). Use `as.matrix()` to get full matrix.
- `"canberra"`: terms with zero numerator and denominator are **omitted** from the sum (not treated as 0/0).
- `Inf` values: Euclidean distance involving `Inf` is `Inf`. Multiple `Inf`s in same obs give `NaN` for some methods.

---

## prcomp vs princomp

- `prcomp` uses **SVD** (numerically superior); `princomp` uses `eigen` on covariance (less stable, N-1 vs N scaling).
- `scale. = TRUE` in `prcomp` standardizes variables; important when variables have very different scales.
- `princomp` standard deviations differ from `prcomp` by factor `sqrt((n-1)/n)`.
- Both return `$rotation` (loadings) and `$x` (scores); sign of components may differ between runs.

---

## density

- Default bandwidth: `bw = "nrd0"` (Silverman's rule of thumb). For multimodal data, consider `"SJ"` or `"bcv"`.
- `adjust`: multiplicative factor on bandwidth. `adjust = 0.5` halves the bandwidth (less smooth).
- Default kernel: `"gaussian"`. Range of density extends beyond data range (controlled by `cut`, default 3 bandwidths).
- `n = 512`: number of evaluation points. Increase for smoother plotting.
- `from`/`to`: explicitly bound the evaluation range.

---

## quantile

- **Nine** `type` options (1-9). Default `type = 7` (R default, linear interpolation). Type 1 = inverse of empirical CDF (SAS default). Types 4-9 are continuous; 1-3 are discontinuous.
- `na.rm = FALSE` by default — returns NA if any NAs present.
- `names = TRUE` by default, adding "0%", "25%", etc. as names.

---

## Distributions (gotchas across all)

All distribution functions follow the `d/p/q/r` pattern. Common non-obvious points:

- **`n` argument in `r*()` functions**: if `length(n) > 1`, uses `length(n)` as the count, not `n` itself. So `rnorm(c(1,2,3))` generates 3 values, not 1+2+3.
- `log = TRUE` / `log.p = TRUE`: compute on log scale for numerical stability in tails.
- `lower.tail = FALSE` gives survival function P(X > x) directly (more accurate than 1 - pnorm() in tails).
- **Gamma**: parameterized by `shape` and `rate` (= 1/scale). Default `rate = 1`. Specifying both `rate` and `scale` is an error.
- **Beta**: `shape1` (alpha), `shape2` (beta) — no `mean`/`sd` parameterization.
- **Poisson `dpois`**: `x` can be non-integer (returns 0 with a warning for non-integer values if `log = FALSE`).
- **Weibull**: `shape` and `scale` (no `rate`). R's parameterization: `f(x) = (shape/scale)(x/scale)^(shape-1) exp(-(x/scale)^shape)`.
- **Lognormal**: `meanlog` and `sdlog` are mean/sd of the **log**, not of the distribution itself.

---

## cor.test

- Default method: `"pearson"`. Also `"kendall"` and `"spearman"`.
- Returns `$estimate`, `$p.value`, `$conf.int` (CI only for Pearson).
- Formula interface: `cor.test(~ x + y, data = df)` — note the `~` with no LHS.

---

## ecdf

- Returns a **function** (step function). Call it on new values: `Fn <- ecdf(x); Fn(3.5)`.
- `plot(ecdf(x))` gives the empirical CDF plot.
- The returned function is right-continuous with left limits (cadlag).

---

## weighted.mean

- Handles `NA` in weights: observation is dropped if weight is `NA`.
- Weights do not need to sum to 1; they are normalized internally.
FILE:references/visualization.md
# Visualization — Quick Reference

> Non-obvious behaviors, gotchas, and tricky defaults for R functions.
> Only what Claude doesn't already know.

---

## par (gotchas)

- `par()` settings are per-device. Opening a new device resets everything.
- Setting `mfrow`/`mfcol` resets `cex` to 1 and `mex` to 1. With 2x2 layout, base `cex` is multiplied by 0.83; with 3+ rows/columns, by 0.66.
- `mai` (inches), `mar` (lines), `pin`, `plt`, `pty` all interact. Restoring all saved parameters after device resize can produce inconsistent results — last-alphabetically wins.
- `bg` set via `par()` also sets `new = FALSE`. Setting `fg` via `par()` also sets `col`.
- `xpd = NA` clips to device region (allows drawing in outer margins); `xpd = TRUE` clips to figure region; `xpd = FALSE` (default) clips to plot region.
- `mgp = c(3, 1, 0)`: controls title line (`mgp[1]`), label line (`mgp[2]`), axis line (`mgp[3]`). All in `mex` units.
- `las`: 0 = parallel to axis, 1 = horizontal, 2 = perpendicular, 3 = vertical. Does **not** respond to `srt`.
- `tck = 1` draws grid lines across the plot. `tcl = -0.5` (default) gives outward ticks.
- `usr` with log scale: contains **log10** of the coordinate limits, not the raw values.
- Read-only parameters: `cin`, `cra`, `csi`, `cxy`, `din`, `page`.

---

## layout

- `layout(mat)` where `mat` is a matrix of integers specifying figure arrangement.
- `widths`/`heights` accept `lcm()` for absolute sizes mixed with relative sizes.
- More flexible than `mfrow`/`mfcol` but cannot be queried once set (unlike `par("mfrow")`).
- `layout.show(n)` visualizes the layout for debugging.

---

## axis / mtext

- `axis(side, at, labels)`: `side` 1=bottom, 2=left, 3=top, 4=right.
- Default gap between axis labels controlled by `par("mgp")`. Labels can overlap if not managed.
- `mtext`: `line` argument positions text in margin lines (0 = adjacent to plot, positive = outward). `adj` controls horizontal position (0-1).
- `mtext` with `outer = TRUE` writes in the **outer** margin (set by `par(oma = ...)`).

---

## curve

- First argument can be an **expression** in `x` or a function: `curve(sin, 0, 2*pi)` or `curve(x^2 + 1, 0, 10)`.
- `add = TRUE` to overlay on existing plot. Default `n = 101` evaluation points.
- `xname = "x"` by default; change if your expression uses a different variable name.

---

## pairs

- `panel` function receives `(x, y, ...)` for each pair. `lower.panel`, `upper.panel`, `diag.panel` for different regions.
- `gap` controls spacing between panels (default 1).
- Formula interface: `pairs(~ var1 + var2 + var3, data = df)`.

---

## coplot

- Conditioning plots: `coplot(y ~ x | a)` or `coplot(y ~ x | a * b)` for two conditioning variables.
- `panel` function can be customized; `rows`/`columns` control layout.
- Default panel draws points; use `panel = panel.smooth` for loess overlay.

---

## matplot / matlines / matpoints

- Plots columns of one matrix against columns of another. Recycles `col`, `lty`, `pch` across columns.
- `type = "l"` by default (unlike `plot` which defaults to `"p"`).
- Useful for plotting multiple time series or fitted curves simultaneously.

---

## contour / filled.contour / image

- `contour(x, y, z)`: `z` must be a matrix with `dim = c(length(x), length(y))`.
- `filled.contour` has a non-standard layout — it creates its own plot region for the color key. **Cannot use `par(mfrow)` with it**. Adding elements requires the `plot.axes` argument.
- `image`: plots z-values as colored rectangles. Default color scheme may be misleading; set `col` explicitly.
- For `image`, `x` and `y` specify **cell boundaries** or **midpoints** depending on context.

---

## persp

- `persp(x, y, z, theta, phi)`: `theta` = azimuthal angle, `phi` = colatitude.
- Returns a **transformation matrix** (invisible) for projecting 3D to 2D — use `trans3d()` to add points/lines to the perspective plot.
- `shade` and `col` control surface shading. `border = NA` removes grid lines.

---

## segments / arrows / rect / polygon

- All take vectorized coordinates; recycle as needed.
- `arrows`: `code = 1` (head at start), `code = 2` (head at end, default), `code = 3` (both).
- `polygon`: last point auto-connects to first. Fill with `col`; `border` controls outline.
- `rect(xleft, ybottom, xright, ytop)` — note argument order is not the same as other systems.

---

## dev / dev.off / dev.copy

- `dev.new()` opens a new device. `dev.off()` closes current device (and flushes output for file devices like `pdf`).
- `dev.off()` on the **last** open device reverts to null device.
- `dev.copy(pdf, file = "plot.pdf")` followed by `dev.off()` to save current plot.
- `dev.list()` returns all open devices; `dev.cur()` the active one.

---

## pdf

- Must call `dev.off()` to finalize the file. Without it, file may be empty/corrupt.
- `onefile = TRUE` (default): multiple pages in one PDF. `onefile = FALSE`: one file per page (uses `%d` in filename for numbering).
- `useDingbats = FALSE` recommended to avoid issues with certain PDF viewers and pch symbols.
- Default size: 7x7 inches. `family` controls font family.

---

## png / bitmap devices

- `res` controls DPI (default 72). For publication: `res = 300` with appropriate `width`/`height` in pixels or inches (with `units = "in"`).
- `type = "cairo"` (on systems with cairo) gives better antialiasing than default.
- `bg = "transparent"` for transparent background (PNG supports alpha).

---

## colors / rgb / hcl / col2rgb

- `colors()` returns all 657 named colors. `col2rgb("color")` returns RGB matrix.
- `rgb(r, g, b, alpha, maxColorValue = 255)` — note `maxColorValue` default is 1, not 255.
- `hcl(h, c, l)`: perceptually uniform color space. Preferred for color scales.
- `adjustcolor(col, alpha.f = 0.5)`: easy way to add transparency.

---

## colorRamp / colorRampPalette

- `colorRamp` returns a **function** mapping [0,1] to RGB matrix.
- `colorRampPalette` returns a **function** taking `n` and returning `n` interpolated colors.
- `space = "Lab"` gives more perceptually uniform interpolation than `"rgb"`.

---

## palette / recordPlot

- `palette()` returns current palette (default 8 colors). `palette("Set1")` sets a built-in palette.
- Integer colors in plots index into the palette (with wrapping). Index 0 = background color.
- `recordPlot()` / `replayPlot()`: save and restore a complete plot — device-dependent and fragile across sessions.
FILE:assets/analysis_template.R
# ============================================================
# Analysis Template — Base R
# Copy this file, rename it, and fill in your details.
# ============================================================
# Author  : 
# Date    : 
# Data    : 
# Purpose : 
# ============================================================


# ── 0. Setup ─────────────────────────────────────────────────
# Clear environment (optional — comment out if loading into existing session)
rm(list = ls())

# Set working directory if needed
# setwd("/path/to/your/project")

# Reproducibility
set.seed(42)

# Libraries — uncomment what you need
# library(haven)        # read .dta / .sav / .sas
# library(readxl)       # read Excel files
# library(openxlsx)     # write Excel files
# library(foreign)      # older Stata / SPSS formats
# library(survey)       # survey-weighted analysis
# library(lmtest)       # Breusch-Pagan, Durbin-Watson etc.
# library(sandwich)     # robust standard errors
# library(car)          # Type II/III ANOVA, VIF


# ── 1. Load Data ─────────────────────────────────────────────
df <- read.csv("your_data.csv", stringsAsFactors = FALSE)
# df <- readRDS("your_data.rds")
# df <- haven::read_dta("your_data.dta")

# First look — always run these
dim(df)
str(df)
head(df, 10)
summary(df)


# ── 2. Data Quality Check ────────────────────────────────────
# Missing values
na_report <- data.frame(
  column   = names(df),
  n_miss   = colSums(is.na(df)),
  pct_miss = round(colMeans(is.na(df)) * 100, 1),
  row.names = NULL
)
print(na_report[na_report$n_miss > 0, ])

# Duplicates
n_dup <- sum(duplicated(df))
cat(sprintf("Duplicate rows: %d\n", n_dup))

# Unique values for categorical columns
cat_cols <- names(df)[sapply(df, function(x) is.character(x) | is.factor(x))]
for (col in cat_cols) {
  cat(sprintf("\n%s (%d unique):\n", col, length(unique(df[[col]]))))
  print(table(df[[col]], useNA = "ifany"))
}


# ── 3. Clean & Transform ─────────────────────────────────────
# Rename columns (example)
# names(df)[names(df) == "old_name"] <- "new_name"

# Convert types
# df$group <- as.factor(df$group)
# df$date  <- as.Date(df$date, format = "%Y-%m-%d")

# Recode values (example)
# df$gender <- ifelse(df$gender == 1, "Male", "Female")

# Create new variables (example)
# df$log_income <- log(df$income + 1)
# df$age_group  <- cut(df$age,
#                      breaks = c(0, 25, 45, 65, Inf),
#                      labels = c("18-25", "26-45", "46-65", "65+"))

# Filter rows (example)
# df <- df[df$year >= 2010, ]
# df <- df[complete.cases(df[, c("outcome", "predictor")]), ]

# Drop unused factor levels
# df <- droplevels(df)


# ── 4. Descriptive Statistics ────────────────────────────────
# Numeric summary
num_cols <- names(df)[sapply(df, is.numeric)]
round(sapply(df[num_cols], function(x) c(
  n      = sum(!is.na(x)),
  mean   = mean(x, na.rm = TRUE),
  sd     = sd(x, na.rm = TRUE),
  median = median(x, na.rm = TRUE),
  min    = min(x, na.rm = TRUE),
  max    = max(x, na.rm = TRUE)
)), 3)

# Cross-tabulation
# table(df$group, df$category, useNA = "ifany")
# prop.table(table(df$group, df$category), margin = 1)  # row proportions


# ── 5. Visualization (EDA) ───────────────────────────────────
par(mfrow = c(2, 2))

# Histogram of main outcome
hist(df$outcome_var,
     main   = "Distribution of Outcome",
     xlab   = "Outcome",
     col    = "steelblue",
     border = "white",
     breaks = 30)

# Boxplot by group
boxplot(outcome_var ~ group_var,
        data = df,
        main = "Outcome by Group",
        col  = "lightyellow",
        las  = 2)

# Scatter plot
plot(df$predictor, df$outcome_var,
     main = "Predictor vs Outcome",
     xlab = "Predictor",
     ylab = "Outcome",
     pch  = 19,
     col  = adjustcolor("steelblue", alpha.f = 0.5),
     cex  = 0.8)
abline(lm(outcome_var ~ predictor, data = df),
       col = "red", lwd = 2)

# Correlation matrix (numeric columns only)
cor_mat <- cor(df[num_cols], use = "complete.obs")
image(cor_mat,
      main = "Correlation Matrix",
      col  = hcl.colors(20, "RdBu", rev = TRUE))

par(mfrow = c(1, 1))


# ── 6. Analysis ───────────────────────────────────────────────

# ·· 6a. Comparison of means ··
t.test(outcome_var ~ group_var, data = df)

# ·· 6b. Linear regression ··
fit <- lm(outcome_var ~ predictor1 + predictor2 + group_var,
          data = df)
summary(fit)
confint(fit)

# Check VIF for multicollinearity (requires car)
# car::vif(fit)

# Robust standard errors (requires lmtest + sandwich)
# lmtest::coeftest(fit, vcov = sandwich::vcovHC(fit, type = "HC3"))

# ·· 6c. ANOVA ··
# fit_aov <- aov(outcome_var ~ group_var, data = df)
# summary(fit_aov)
# TukeyHSD(fit_aov)

# ·· 6d. Logistic regression (binary outcome) ··
# fit_logit <- glm(binary_outcome ~ x1 + x2,
#                  data   = df,
#                  family = binomial(link = "logit"))
# summary(fit_logit)
# exp(coef(fit_logit))         # odds ratios
# exp(confint(fit_logit))      # OR confidence intervals


# ── 7. Model Diagnostics ─────────────────────────────────────
par(mfrow = c(2, 2))
plot(fit)
par(mfrow = c(1, 1))

# Residual normality
shapiro.test(residuals(fit))

# Homoscedasticity (requires lmtest)
# lmtest::bptest(fit)


# ── 8. Save Output ────────────────────────────────────────────
# Cleaned data
# write.csv(df, "data_clean.csv", row.names = FALSE)
# saveRDS(df, "data_clean.rds")

# Model results to text file
# sink("results.txt")
# cat("=== Linear Model ===\n")
# print(summary(fit))
# cat("\n=== Confidence Intervals ===\n")
# print(confint(fit))
# sink()

# Plots to file
# png("figure1_distributions.png", width = 1200, height = 900, res = 150)
# par(mfrow = c(2, 2))
# # ... your plots ...
# par(mfrow = c(1, 1))
# dev.off()

# ============================================================
# END OF TEMPLATE
# ============================================================
FILE:scripts/check_data.R
# check_data.R — Quick data quality report for any R data frame
# Usage: source("check_data.R") then call check_data(df)
# Or:    source("check_data.R"); check_data(read.csv("yourfile.csv"))

check_data <- function(df, top_n_levels = 8) {
  
  if (!is.data.frame(df)) stop("Input must be a data frame.")
  
  n_row <- nrow(df)
  n_col <- ncol(df)
  
  cat("══════════════════════════════════════════\n")
  cat("  DATA QUALITY REPORT\n")
  cat("══════════════════════════════════════════\n")
  cat(sprintf("  Rows: %d    Columns: %d\n", n_row, n_col))
  cat("══════════════════════════════════════════\n\n")
  
  # ── 1. Column overview ──────────────────────
  cat("── COLUMN OVERVIEW ────────────────────────\n")
  
  for (col in names(df)) {
    x     <- df[[col]]
    cls   <- class(x)[1]
    n_na  <- sum(is.na(x))
    pct   <- round(n_na / n_row * 100, 1)
    n_uniq <- length(unique(x[!is.na(x)]))
    
    na_flag <- if (n_na == 0) "" else sprintf("  *** %d NAs (%.1f%%)", n_na, pct)
    cat(sprintf("  %-20s  %-12s  %d unique%s\n",
                col, cls, n_uniq, na_flag))
  }
  
  # ── 2. NA summary ────────────────────────────
  cat("\n── NA SUMMARY ─────────────────────────────\n")
  
  na_counts <- sapply(df, function(x) sum(is.na(x)))
  cols_with_na <- na_counts[na_counts > 0]
  
  if (length(cols_with_na) == 0) {
    cat("  No missing values. \n")
  } else {
    cat(sprintf("  Columns with NAs: %d of %d\n\n", length(cols_with_na), n_col))
    for (col in names(cols_with_na)) {
      bar_len  <- round(cols_with_na[col] / n_row * 20)
      bar      <- paste0(rep("█", bar_len), collapse = "")
      pct_na   <- round(cols_with_na[col] / n_row * 100, 1)
      cat(sprintf("  %-20s  [%-20s]  %d (%.1f%%)\n",
                  col, bar, cols_with_na[col], pct_na))
    }
  }
  
  # ── 3. Numeric columns ───────────────────────
  num_cols <- names(df)[sapply(df, is.numeric)]
  
  if (length(num_cols) > 0) {
    cat("\n── NUMERIC COLUMNS ────────────────────────\n")
    cat(sprintf("  %-20s  %8s  %8s  %8s  %8s  %8s\n",
                "Column", "Min", "Mean", "Median", "Max", "SD"))
    cat(sprintf("  %-20s  %8s  %8s  %8s  %8s  %8s\n",
                "──────", "───", "────", "──────", "───", "──"))
    
    for (col in num_cols) {
      x  <- df[[col]][!is.na(df[[col]])]
      if (length(x) == 0) next
      cat(sprintf("  %-20s  %8.3g  %8.3g  %8.3g  %8.3g  %8.3g\n",
                  col,
                  min(x), mean(x), median(x), max(x), sd(x)))
    }
  }
  
  # ── 4. Factor / character columns ───────────
  cat_cols <- names(df)[sapply(df, function(x) is.factor(x) | is.character(x))]
  
  if (length(cat_cols) > 0) {
    cat("\n── CATEGORICAL COLUMNS ────────────────────\n")
    
    for (col in cat_cols) {
      x    <- df[[col]]
      tbl  <- sort(table(x, useNA = "no"), decreasing = TRUE)
      n_lv <- length(tbl)
      cat(sprintf("\n  %s  (%d unique values)\n", col, n_lv))
      
      show <- min(top_n_levels, n_lv)
      for (i in seq_len(show)) {
        lbl <- names(tbl)[i]
        cnt <- tbl[i]
        pct <- round(cnt / n_row * 100, 1)
        cat(sprintf("    %-25s  %5d  (%.1f%%)\n", lbl, cnt, pct))
      }
      if (n_lv > top_n_levels) {
        cat(sprintf("    ... and %d more levels\n", n_lv - top_n_levels))
      }
    }
  }
  
  # ── 5. Duplicate rows ────────────────────────
  cat("\n── DUPLICATES ─────────────────────────────\n")
  n_dup <- sum(duplicated(df))
  if (n_dup == 0) {
    cat("  No duplicate rows.\n")
  } else {
    cat(sprintf("  %d duplicate row(s) found (%.1f%% of data)\n",
                n_dup, n_dup / n_row * 100))
  }
  
  cat("\n══════════════════════════════════════════\n")
  cat("  END OF REPORT\n")
  cat("══════════════════════════════════════════\n")
  
  # Return invisibly for programmatic use
  invisible(list(
    dims       = c(rows = n_row, cols = n_col),
    na_counts  = na_counts,
    n_dupes    = n_dup
  ))
}
FILE:scripts/scaffold_analysis.R
#!/usr/bin/env Rscript
# scaffold_analysis.R — Generates a starter analysis script
#
# Usage (from terminal):
#   Rscript scaffold_analysis.R myproject
#   Rscript scaffold_analysis.R myproject outcome_var group_var
#
# Usage (from R console):
#   source("scaffold_analysis.R")
#   scaffold_analysis("myproject", outcome = "score", group = "treatment")
#
# Output: myproject_analysis.R  (ready to edit)

scaffold_analysis <- function(project_name,
                               outcome   = "outcome",
                               group     = "group",
                               data_file = NULL) {
  
  if (is.null(data_file)) data_file <- paste0(project_name, ".csv")
  out_file <- paste0(project_name, "_analysis.R")
  
  template <- sprintf(
'# ============================================================
# Project : %s
# Created : %s
# ============================================================

# ── 0. Libraries ─────────────────────────────────────────────
# Add packages you need here
# library(ggplot2)
# library(haven)     # for .dta files
# library(openxlsx)  # for Excel output


# ── 1. Load Data ─────────────────────────────────────────────
df <- read.csv("%s", stringsAsFactors = FALSE)

# Quick check — always do this first
cat("Dimensions:", dim(df), "\\n")
str(df)
head(df)


# ── 2. Explore / EDA ─────────────────────────────────────────
summary(df)

# NA check
na_counts <- colSums(is.na(df))
na_counts[na_counts > 0]

# Key variable distributions
hist(df$%s, main = "Distribution of %s", xlab = "%s")

if ("%s" %%in%% names(df)) {
  table(df$%s)
  barplot(table(df$%s),
          main = "Counts by %s",
          col  = "steelblue",
          las  = 2)
}


# ── 3. Clean / Transform ──────────────────────────────────────
# df <- df[complete.cases(df), ]        # drop rows with any NA
# df$%s <- as.factor(df$%s)            # convert to factor


# ── 4. Analysis ───────────────────────────────────────────────

# Descriptive stats by group
tapply(df$%s, df$%s, mean, na.rm = TRUE)
tapply(df$%s, df$%s, sd,   na.rm = TRUE)

# t-test (two groups)
# t.test(%s ~ %s, data = df)

# Linear model
fit <- lm(%s ~ %s, data = df)
summary(fit)
confint(fit)

# ANOVA (multiple groups)
# fit_aov <- aov(%s ~ %s, data = df)
# summary(fit_aov)
# TukeyHSD(fit_aov)


# ── 5. Visualize Results ──────────────────────────────────────
par(mfrow = c(1, 2))

# Boxplot by group
boxplot(%s ~ %s,
        data = df,
        main = "%s by %s",
        xlab = "%s",
        ylab = "%s",
        col  = "lightyellow")

# Model diagnostics
plot(fit, which = 1)  # residuals vs fitted

par(mfrow = c(1, 1))


# ── 6. Save Output ────────────────────────────────────────────
# Save cleaned data
# write.csv(df, "%s_clean.csv", row.names = FALSE)

# Save model summary to text
# sink("%s_results.txt")
# summary(fit)
# sink()

# Save plot to file
# png("%s_boxplot.png", width = 800, height = 600, res = 150)
# boxplot(%s ~ %s, data = df, col = "lightyellow")
# dev.off()
',
    project_name,
    format(Sys.Date(), "%%Y-%%m-%%d"),
    data_file,
    # Section 2 — EDA
    outcome, outcome, outcome,
    group, group, group, group,
    # Section 3
    group, group,
    # Section 4
    outcome, group,
    outcome, group,
    outcome, group,
    outcome, group,
    outcome, group,
    outcome, group,
    # Section 5
    outcome, group,
    outcome, group,
    group, outcome,
    # Section 6
    project_name, project_name, project_name,
    outcome, group
  )
  
  writeLines(template, out_file)
  cat(sprintf("Created: %s\n", out_file))
  invisible(out_file)
}


# ── Run from command line ─────────────────────────────────────
if (!interactive()) {
  args <- commandArgs(trailingOnly = TRUE)
  
  if (length(args) == 0) {
    cat("Usage: Rscript scaffold_analysis.R <project_name> [outcome_var] [group_var]\n")
    cat("Example: Rscript scaffold_analysis.R myproject score treatment\n")
    quit(status = 1)
  }
  
  project <- args[1]
  outcome <- if (length(args) >= 2) args[2] else "outcome"
  group   <- if (length(args) >= 3) args[3] else "group"
  
  scaffold_analysis(project, outcome = outcome, group = group)
}
FILE:README.md
# base-r-skill 

GitHub: https://github.com/iremaydas/base-r-skill

A Claude Code skill for base R programming.

---

## The Story

I'm a political science PhD candidate who uses R regularly but would never call myself *an R person*. I needed a Claude Code skill for base R — something without tidyverse, without ggplot2, just plain R — and I couldn't find one anywhere.

So I made one myself. At 11pm. Asking Claude to help me build a skill for Claude. 

If you're also someone who Googles `how to drop NA rows in R` every single time, this one's for you. 🫶

---

## What's Inside

```
base-r/
├── SKILL.md                    # Main skill file
├── references/                 # Gotchas & non-obvious behaviors
│   ├── data-wrangling.md       # Subsetting traps, apply family, merge, factor quirks
│   ├── modeling.md             # Formula syntax, lm/glm/aov/nls, optim
│   ├── statistics.md           # Hypothesis tests, distributions, clustering
│   ├── visualization.md        # par, layout, devices, colors
│   ├── io-and-text.md          # read.table, grep, regex, format
│   ├── dates-and-system.md     # Date/POSIXct traps, options(), file ops
│   └── misc-utilities.md       # tryCatch, do.call, time series, utilities
├── scripts/
│   ├── check_data.R            # Quick data quality report for any data frame
│   └── scaffold_analysis.R     # Generates a starter analysis script
└── assets/
    └── analysis_template.R     # Copy-paste analysis template
```

The reference files were condensed from the official R 4.5.3 manual — **19,518 lines → 945 lines** (95% reduction). Only the non-obvious stuff survived: gotchas, surprising defaults, tricky interactions. The things Claude already knows well got cut.

---

## How to Use

Add this skill to your Claude Code setup by pointing to this repo. Then Claude will automatically load the relevant reference files when you're working on R tasks.

Works best for:
- Base R data manipulation (no tidyverse)
- Statistical modeling with `lm`, `glm`, `aov`
- Base graphics with `plot`, `par`, `barplot`
- Understanding why your R code is doing that weird thing

Not for: tidyverse, ggplot2, Shiny, or R package development.

---

## The `check_data.R` Script

Probably the most useful standalone thing here. Source it and run `check_data(df)` on any data frame to get a formatted report of dimensions, NA counts, numeric summaries, and categorical breakdowns.

```r
source("scripts/check_data.R")
check_data(your_df)
```

---

## Built With Help From

- Claude (obviously)
- The official R manuals (all 19,518 lines of them)
- Mild frustration and several cups of coffee

---

## Contributing

If you spot a missing gotcha, a wrong default, or something that should be in the references — PRs are very welcome. I'm learning too.

---

*Made by [@iremaydas](https://github.com/iremaydas) — PhD candidate, occasional R user, full-time Googler of things I should probably know by now.*
