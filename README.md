# bus-based-arq-simulation

Console arq system simulation created for the course digital device reliability and diagnostics
## Run Locally

- clone the entire repository
```bash
  git clone https://github.com/Ernest-K/bus-based-arq-simulation.git
```
- run project 
```bash
  cd bus-based-arq-simulation
  python main.py
```
## Usage/Examples
Input parameters can be specified in [main.py](main.py):
- Number of transmitters
- Size of message [b]
- Size of packet [b]
- Bandwidth [bps]

```python
  Simulator([number-of-transmitters], [message-size], [packet-size], [bandwidth])
```

Example:
```python
  Simulator(10, 512, 256, 64)
```
