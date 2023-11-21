def directions():
  directions = ["Move Forward","Move Backward", "Turn Left", "Turn Right"]
  return directions
def run():
  run_dir = directions()
  print(run_dir)


if __name__ == "__main__":
  run()

def movements():
  path = ["Move Forward", 10,"Move Backward", 5,"Move Left", 3,"Move Right", 1]
  return path
def run():
  print("Moving...")
  run_mov = movements()
  print(f"{run_mov[0]} for {run_mov[1]} steps")
  print(f"{run_mov[2]} for {run_mov[3]} steps")
  print(f"{run_mov[4]} for {run_mov[5]} steps")
  print(f"{run_mov[6]} for {run_mov[7]} steps")

run()



 def pattern():
    sequences = {
        "Short Sequence":3,
        "Medium Sequence":2,
        "Long Sequence":1
    }
    return sequences
  def run():
    run_seq = pattern()
    print(run_seq)


  if __name__ == "__main__":
    run()
  def display_keys():
    keys_seq = pattern()
    keysList = list(keys_seq.keys())
    print("Keys:")
    print(keysList[0])
    print(keysList[1])
    print(keysList[2])
  display_keys()

  def display_values():
    values_seq = pattern()
    valuesList = list(values_seq.values())
    print("Values:")
    print(valuesList[0])
    print(valuesList[1])
    print(valuesList[2])
  display_values()
    
  def display_items():
    items_seq = pattern()
    keysList = list(items_seq.keys())
    valuesList = list(items_seq.values())
    print("Items:")
    print(f"{keysList[0]}: {valuesList[0]}")
    print(f"{keysList[1]}: {valuesList[1]}")
    print(f"{keysList[2]}: {valuesList[2]}")
  display_items()