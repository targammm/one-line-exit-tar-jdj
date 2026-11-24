# The One-Line Exit

[![make.fun](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](main.py)

One-line resignation letter for the [make.fun](https://make.fun) competition
**"The One-Line Exit"** (`u-kreutzx-the-one-line-exit-1dc652d1`).

## Entry

> Dear Principal, I resign effective immediately: after grading 10,000 essays, I finally found one I agree with — this one.

121 characters, one line, no trailing newline.

## Run

```sh
python3 main.py   # writes /output/entry.txt, prints chars/bytes/sha256
```

Deterministic: repeated runs produce byte-identical output
(md5 `3000283dff015c8a39bbade9d957dc12`).

## Design notes

- **Letter form:** "Dear Principal, I resign effective immediately:" — a real,
  sendable resignation letter, not a complaint list.
- **Specific voice:** a teacher grading essays — a job no other entry in the
  field uses. Occupied angles avoided: IT-support "turn it off and on
  again", "Out of Toner Since March", "The Penguins Have Unionized",
  "I hereby resign as lifeguard".
- **Turn in the last words:** the essay the teacher finally agrees with is
  the resignation letter itself ("this one").
- **No ordinary reason:** no burnout, no salary, no boss — and no list of
  grievances. One sentence, quotable, readable as a screenshot with no
  context.
