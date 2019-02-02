import sys
if sys.version_info[0] != 3 or sys.version_info[1] < 4:
    print("This script requires Python version >=3.4")
    sys.exit(1)

import csv
import argparse
import subprocess
import statistics

# TODO creating a latex table

instances = [
  (10, 360, 120),
  (12, 200, 75),
  (9, 300, 100),
  (15, 350, 100),
  (10, 325, 100),
  (13, 250, 80),
  (10, 350, 100),
  (9, 70, 35),
  (11, 150, 50),
  (6, 60, 30),
  (6, 50, 25),
  (10, 100, 30),
  (8, 28, 14),
  (10, 37, 14),
  (19, 19, 9),
  (11, 22, 10),
  (9, 36, 12),
  (16, 16, 6),
  # (15, 21, 7), # Lambda = 2, best known solution = 3
  (12, 44, 11),
  (10, 30, 9)
]


def main():
  # Parse arguments
  parser = argparse.ArgumentParser(description='Run experiments.')

  parser.add_argument('executable',
    type=str,
    nargs='?',
    default='../build/invDes',
    help='Path to the executable')

  parser.add_argument(
    '-n',
    '--runs',
    type=int,
    default=5,
    help='How many times to run each instance')

  parser.add_argument('-p', '--parameters',
    type=str,
    default='',
    help='The parameters to pass to the executable')

  parser.add_argument('-i', '--instances',
    type=int,
    nargs='*',
    default=range(0,len(instances)),
    help='Which instances to run (default: all)')

  args = parser.parse_args()
  
  # Run experiments
  results = []
  for instance in [instances[i] for i in args.instances]:
    print(instance)
    v, b, r = instance
    runtimes, steps, obj = [], [], []

    for i in range(args.runs):
      print(i+1, '/',  args.runs)
      out = subprocess.run([
          args.executable,
          str(v),
          str(b),
          str(r),
          '--print-stats',  # replace for your -p flag
          args.parameters,
        ],
        check=True,
        stdout=subprocess.PIPE,
      ).stdout.decode('utf-8').split(' ')

      runtimes.append(float(out[0]))
      steps.append(int(out[1]))
      obj.append(int(out[2]))
        
    results.append({
      'v': v,
      'b': b,
      'r': r,
      'runtime': round(statistics.median(runtimes), 1),
      'steps': statistics.median(steps),
      'obj': statistics.median(obj),
    })

  # Write in csv format to std out
  writer = csv.DictWriter(sys.stdout, fieldnames=results[0].keys())
  writer.writeheader()
  for row in results:
    writer.writerow(row)


if __name__ == '__main__':
  main()