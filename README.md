# tiny-chess-01

A chess engine in at most 4,096 bytes of Python for the make.fun bounty
"Build the strongest chess engine in 4 KB of Python".

`main.py` is the whole engine: a 0x88 alpha-beta search with quiescence,
transposition table and killer-move ordering, a fixed node budget per move
(never a clock), talking to the env at `MAKEFUN_ENV_URL` (`POST /game`,
`POST /move`) and sending moves in UCI.

Run: `MAKEFUN_ENV_URL=http://127.0.0.1:18080 python3 main.py`
