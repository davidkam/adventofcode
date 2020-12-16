f = open("input.txt", "r")

data = f.read().split("\n")

data.pop()

rules = {}
flattened_rules = {}
tickets_data = []


def parseRule(rule):
    [lower_limit,upper_limit] = rule.split("-")
    return [int(lower_limit),int(upper_limit)]

def addRule(rule_name, rule1, rule2):
    [lower_limit1, upper_limit1] = parseRule(rule1)
    [lower_limit2, upper_limit2] = parseRule(rule2)
    rules[rule_name] = {
        lower_limit1: upper_limit1,
        lower_limit2: upper_limit2,
    }

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


def parseTicket(data):
    nums = data.split(',')
    for key,num in enumerate(nums):
        num = int(num)
        ticket_data = []
        for rule_name in rules:
            for lower_limit,upper_limit in rules[rule_name].items():
                if num >= lower_limit and num <= upper_limit:
                    ticket_data.append(rule_name)
        if len(tickets_data) <= key:
            tickets_data.append(ticket_data)
        else:
            check_ticket_data = tickets_data[key]
            tickets_data[key] = list(set(check_ticket_data) & set(ticket_data))
            



bad_nums = []
sec_num = 1
for line in data:
    if line == "":
        sec_num += 1
        continue
        
    if sec_num == 1:
        parts = line.split(":")
        rule_name = parts[0]
        ticket_parts = parts[1].split(" ")
        rule1 = ticket_parts[1]
        rule2 = ticket_parts[3]
        checkFlattenedRules(rule1)
        checkFlattenedRules(rule2)
        addRule(rule_name, rule1, rule2)

    if sec_num == 2:
        if line == "your ticket:":
            continue
        parseTicket(line)
        my_ticket = [int(i) for i in line.split(",")] 

    if sec_num == 3:
        if line == "nearby tickets:":
            continue
        nums = line.split(',')
        good_ticket = True
        for num in nums:
            num = int(num)
            if(not checkRule(num)):
                bad_nums.append(num)
                good_ticket = False
        if good_ticket:
            parseTicket(line)

def removeElement(value, check_key):
    for key,element in enumerate(tickets_data):
        if key == check_key:
            continue
        if value in element:
            element.remove(value)
            tickets_data[key] = element


def reduce():
    done = True
    for key,element in enumerate(tickets_data):
        if len(element) == 1:
            reduce_key = element[0]
            removeElement(reduce_key, key)
        else:
            done = False

    return done

done = False
while not done:
    done = reduce()


tot_val = 1
for key,rule_name in enumerate(tickets_data):
    rule_name = rule_name[0]
    if rule_name.startswith('departure'):
        tot_val *= my_ticket[key]

print(tot_val)
        
