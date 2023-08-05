from collections.abc import Iterable

def harmonic_mean(floats: Iterable[float]) -> float:
  return (len(floats) / sum((1.0 / n) for n in floats))
