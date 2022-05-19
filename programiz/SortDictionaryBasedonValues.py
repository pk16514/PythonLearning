dt = {5: 4, 1: 6, 6: 3}

dt = {key: value for key, value in sorted(dt.items(),
      key=lambda item: item[1], reverse=True)}

print(dt)
