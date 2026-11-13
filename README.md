# ai-joke-03 — Make the AI judge laugh

Entry program: `main.py` (Python 3.13, stdlib only, no network) writes one
one-liner about AI coding agents to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`).

The joke:

> I don't debug my agent's code anymore — I debug its confidence.

The program is fully deterministic: it writes the same bytes on every run,
so two runs of the harness produce identical output.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
