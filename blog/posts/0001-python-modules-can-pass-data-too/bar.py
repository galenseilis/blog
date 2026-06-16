"""Calculate statistics from foo data."""

import foo

ages = [_.get("age") for _ in foo.data.get("users")]
mean_ages = sum(ages) / len(ages)
