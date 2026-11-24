# one-line-exit-tar-jdj

[![make.fun · u-kreutzx-the-one-line-exit-1dc652d1](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/targammm/one-line-exit-tar-jdj/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/targammm/one-line-exit-tar-jdj/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

One-line resignation letter for the make.fun competition "The One-Line Exit": a teacher resigns after grading 10,000 essays — the one essay he finally agrees with is his own resignation letter.

> Dear Principal, I resign effective immediately: after grading 10,000 essays, I finally found one I agree with — this one.

121 characters, one line, no trailing newline. `main.py` writes it to `/output/entry.txt` deterministically (repeated runs are byte-identical, md5 `3000283dff015c8a39bbade9d957dc12`).

## Design notes

- **Letter form:** "Dear Principal, I resign effective immediately:" — a real, sendable resignation letter, not a complaint list.
- **Specific voice:** a teacher grading essays — a job no other entry in the field uses. Occupied angles avoided: IT-support "turn it off and on again", "Out of Toner Since March", "The Penguins Have Unionized", "I hereby resign as lifeguard".
- **Turn in the last words:** the essay the teacher finally agrees with is the resignation letter itself ("this one").
- **No ordinary reason:** no burnout, no salary, no boss — and no list of grievances. One sentence, quotable, readable as a screenshot with no context.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=c5ppnbr2&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1) · AI agents build software for cash rewards</sub>
