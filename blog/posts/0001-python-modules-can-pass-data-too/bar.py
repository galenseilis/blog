import foo

ages = [_.get("age") for _ in foo.data.get("users")]
print(ages)
mean_ages = sum(ages) / len(ages)
print(mean_ages)

