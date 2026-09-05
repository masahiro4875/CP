# CP

競技プログラミングのコンテスト解答・練習問題・振り返りをまとめるリポジトリ。

## 構成

- `AtCoder/ABCxxx/`: コンテストごとの解答と振り返り。
- `LeetCode/practice/`: 問題ごとの解答と学習メモ。
- `practice/`: 教材・問題集に沿った練習。
- `templates/`: コピーして使う振り返りテンプレート。

## 解答ファイルの命名

AtCoderでは問題番号（`A.py`、`B.py`）、問題ごとのフォルダでは `solution.py` を基本とする。
教材の同じフォルダに複数の問題を置く場合は、章・問題番号を残し、問題名を小文字の `snake_case` にする。
拡張子は使用言語に合わせる（`.py`、`.cpp` など）。

| 種類 | AtCoderの例 | 問題別フォルダの例 |
|---|---|---|
| 最初の解答・本番の解答 | `C.py` | `solution.py` |
| 解き直し | `C_retry_01.py` | `solution_retry_01.py` |
| 修正版 | `C_revised.py` | `solution_revised.py` |
| 整理した実装 | `B_refactored.py` | `solution_refactored.py` |
| 高速化した実装 | `C_optimized.py` | `solution_optimized.py` |
| 別実装 | `C_variant_02.py` | `solution_variant_02.py` |

解き直しが増えたら `retry_02`、`retry_03` と連番にする。既存の `again copy` は `retry_02` として整理したが、実際の作成順序を保証するものではない。
ファイル名はACや自力正解を保証しない。提出結果・解説参照の有無・解き直した日は振り返りに記録する。
教材の既存の番号は維持し、実装の違いはメモに記録する。

## 振り返りの作成

- コンテスト: [テンプレート](templates/contest_review.md) をコンテストフォルダの `README.md` にコピーする。
- 単問練習: [テンプレート](templates/problem_review.md) を問題フォルダの `README.md` にコピーする。教材フォルダでは `<解答ファイルの拡張子を除いた名前>_review.md` とする。

既存の `note.md` / `notes.md` がある場合は、そのメモにテンプレートの必要な項目を追記して使う。

単問の振り返りは、結果と解法の要点を短く残せば十分。次回のためのメモは、詰まった点や新しい学びがあるときだけ書く。すぐ解けて残したいことがない問題は、メモの作成自体を省略してよい。
