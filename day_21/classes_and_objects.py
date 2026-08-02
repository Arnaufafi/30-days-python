# Day 21 - 30DaysOfPython Challenge

## LEVEL 1

class Statistics():

    def __init__(self, input_numbers):
        self.numbers = input_numbers

    def count(self):
        return len(self.numbers)

    def sum(self):
        return sum(self.numbers)

    def min(self):
        return min(self.numbers)

    def max(self):
        return max(self.numbers)

    def range(self):
        return max(self.numbers) - min(self.numbers)

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        nums = sorted(self.numbers)
        n = len(nums)
        mid = n //2

        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[mid]

    def mode(self):
        nums = sorted(self.numbers)
        popular = None
        max_count = 0
        actual = None
        count = 0
        for n in nums:
            if n != actual:
                actual = n
                count = 1
            else:
                count += 1

            if count > max_count:
                popular = n
                max_count = count

        return {"mode" : popular, "count" : max_count}

    def std(self):
        return self.var()**(0.5)

    def var(self):
        mean = self.mean()
        numbers = [n - mean for n in self.numbers]
        sqr_numbers = [n*n for n in numbers]
        return sum(sqr_numbers) / len(self.numbers)

    def freq_dist(self):
        freq_dist = {}
        for n in self.numbers:
            if n not in freq_dist:
                freq_dist[n] = 1
            else:
                freq_dist[n] += 1

        return freq_dist

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist())

## LEVEL 2

class Person():

    def __init__(self, firstname, lastname):

        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description,0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description,0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Account Holder: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Balance: {self.account_balance()}\n"
        info += "Incomes:\n"
        for desc, amt in self.incomes.items():
            info += f"\t - {desc}: {amt}\n"
        info += "Expenses:\n"
        for desc, amt in self.expenses.items():
            info += f"\t - {desc}: {amt}\n"

        return info
