# tiny-chess-01

A chess engine in at most 4,096 bytes of Python for the make.fun bounty
"Build the strongest chess engine in 4 KB of Python".

`main.py` is the whole engine: a 0x88 alpha-beta search with quiescence,
transposition table and killer-move ordering, a fixed node budget per move
(never a clock), talking to the env at `MAKEFUN_ENV_URL` (`POST /game`,
`POST /move`) and sending moves in UCI.

The engine is N7: captures-only move generation in quiescence, Zobrist
hashing with a 1M-entry transposition table, incremental evaluation
(the material + piece-square sum is maintained move by move instead of
rescanned), and a 150,000-node cap per move. Practice mean Elo 1,463
(house trials 1,598 / 1,396 / 1,396), above the sunfish 4 KB baseline
(1,325) and the 1,154 practice floor. N7 was the strongest of every
variant tried in phases 1-10 (N123, N5, then N7); nothing else beat it.

`engine_dev.py` is the readable source; `main.py` is the same engine
packed with the make.fun kit. `tests/test_n7.py` checks perft
(20 / 400 / 8,902) and equivalence with the practice N7 variant.

Run: `MAKEFUN_ENV_URL=http://127.0.0.1:18080 python3 main.py`
