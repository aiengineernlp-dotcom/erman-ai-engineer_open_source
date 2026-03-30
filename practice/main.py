# main.py
"""
PROJECT: AI Environment Validator
Author : Erman
Date   : 2026-03-30
Description : Validates the Ml Environment Setup
"""


def check_environment()->dict:
    packages = {
        "numpy":False,
        "matplotlib":False,
        "pandas":False,
        "sklearn":False,
        "jupytr":False,
    }

    for package  in  packages:
        try:
            __import__(package) # ici on verifie si le package est present dans le module "__import__"
            packages[package] = True
        except ImportError:
            packages[package] = False
    return packages

x=check_environment()
print(x)



def display_report(env_status: dict) -> None:
    """Display Environment Status Report"""
    print("=" * 140)
    print("    ML ENVIRONMENT STATUS REPORT")
    print("=" * 140)

    for package, status in env_status.items():
        icon = "✅" if status else "❌"
        print(f"    {icon}    {package:<15} {'OK' if status else 'MISSING'}")

    print("=" * 140)
    total = sum(env_status.values())
    print(f"    Score: {total}/{len(env_status)} packages ready")


'''Regarde cette suggestion commentee '''
    # results = check_environment()
    # print(f"{'PACKAGE':<15} | {'STATUS'}")
    # print("-" * 25)
    # for pkg, status in results.items():
    #     emoji = "✅" if status else "❌"
    #     print(f"{pkg:<15} | {emoji}")


if __name__=="__main__":
    status = check_environment()
    display_report(status)
