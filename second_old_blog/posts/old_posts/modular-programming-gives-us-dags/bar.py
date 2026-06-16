import foo

print(f"{foo.data=} from {__file__}")
data = foo.data.copy()
data.update({10})
print(f"{data=} from {__file__}")
