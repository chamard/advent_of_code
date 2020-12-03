import glob
import sys

def print_solutions(days):
    for day in sorted(days):
        class_name =  f'SolutionsDay{day}'
        mod = __import__(f'{day}.solutions', fromlist=[class_name])
        solution_class = getattr(mod, class_name)

        print(class_name)
        solution_class().print_solutions()
        print()


if __name__ == '__main__':
    days = set(glob.glob('[0-9]'))
    input_days = set(sys.argv[1:])
    if input_days:
        days = days.intersection(input_days)
    print_solutions(days)
