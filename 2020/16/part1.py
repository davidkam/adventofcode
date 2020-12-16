f = open("input.txt", "r")

data = f.read().split("\n")

data.pop()

rules = {}
flattened_rules = {}


def parseRule(rule):
    [lower_limit,upper_limit] = rule.split("-")
    return [int(lower_limit),int(upper_limit)]

def checkRule(num):
    for lower_limit in flattened_rules:
        upper_limit = flattened_rules[lower_limit]
        if num >= lower_limit and num <= upper_limit:
            return True
    return False

def checkFlattenedRules(rule_check):
    [lower_limit, upper_limit] = parseRule(rule_check)
    new_lower_limit = None
    new_upper_limit = None
    to_remove = []
    for check_lower_limit in flattened_rules:
        check_upper_limit = flattened_rules[check_lower_limit]
        if lower_limit >= check_lower_limit:
            if lower_limit >= check_lower_limit and lower_limit <= check_upper_limit:
                new_lower_limit = check_lower_limit
                if upper_limit > check_upper_limit:
                    new_upper_limit = upper_limit
            if lower_limit > check_upper_limit:
                new_lower_limit = lower_limit
                new_upper_limit = upper_limit

        if lower_limit < check_lower_limit:
            new_lower_limit = lower_limit
            if upper_limit < check_lower_limit:
                new_uper_limit = upper_limit
            else:
                to_remove.append(check_lower_limit)
                if upper_limit <= check_upper_limit:
                    new_upper_limit = check_upper_limit
                else:
                    new_upper_limit = upper_limit
                
    for remove_key in to_remove:
        del flattened_rules[remove_key]
    if new_lower_limit is not None and new_upper_limit is not None:
        flattened_rules[new_lower_limit] = new_upper_limit
    if new_lower_limit is None and new_upper_limit is None:
        flattened_rules[lower_limit] = upper_limit



bad_nums = []
sec_num = 1
for line in data:
    if line == "":
        sec_num += 1
        continue
        
    if sec_num == 1:
        parts = line.split(":")[1].split(" ")
        rule1 = parts[1]
        rule2 = parts[3]
        checkFlattenedRules(rule1)
        checkFlattenedRules(rule2)

    if sec_num == 3:
        if line == "nearby tickets:":
            continue
        nums = line.split(',')
        good_ticket = True
        for num in nums:
            num = int(num)
            if(not checkRule(num)):
                bad_nums.append(num)

print(sum(bad_nums))
