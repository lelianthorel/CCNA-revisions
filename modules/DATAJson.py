from colorama import Fore, Style
from rich.console import Console

console = Console()

class DATAJson:
    
    def __init__(self , ANSWERS):
        self.ANSWERS = ANSWERS
    
    def get_result(self):
        if len(self.ANSWERS) > 1:
            user_answer = input("Veuillez choisir les bonnes réponses (séparées par des espaces) : ").split()
        else:
            user_answer = input("Veuillez choisir la bonne réponse : ").split()
            if len(user_answer) > 1:
                console.print("[bold red]Vous ne devez choisir qu'une seule réponse.[/bold red]")
                return False
        
        if self.is_good_a_answer(user_answer):
            return True
        
        return False
    
        
    def is_good_a_answer(self, user_answer):
        count = 0
        pass_answer = []
        
        for answer in user_answer:
            try:
                if int(answer) in self.ANSWERS and int(answer) not in pass_answer:
                    count += 1
                    pass_answer.append(int(answer))
                    
            except ValueError:
                print(f"{Style.DIM}{Fore.RED}MERCI de spécifier une valeur correcte.{Style.RESET_ALL}")
                return self.get_result()
                
        return count == len(self.ANSWERS)
