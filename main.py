def ribs(*args, **fwargs):
  first, second = args[0],args[1]
  if first**3 == second**3:
    return"equal"
  return first if first**3 > second**3 else second
if __name__ == "__main__":
  print(ribs(5, 5))