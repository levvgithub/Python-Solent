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



firstdic = {
  "brand": "Apple",
  "model": "iPhone",
  "ram_capacity": "4GB",
  "market_regions": "Russia",
  "info_added_date": "11/11/2023"
}
print(firstdic["brand"])
print(firstdic["model"])
print(firstdic["ram_capacity"])
print(firstdic["market_regions"])
print(firstdic["info_added_date"])