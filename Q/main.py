class Job:
    def __init__(self, name: str) -> None:
        self.name = name
        self.companys = {}

    def post_vacancy(self, company, salary, min_exp):
        self.companys[company] = [salary, min_exp]

    def close_vacancy(self, company):
        self.companys.pop(company)

    def update_salary(self, company, new_salary):
        self.companys[company][0] = new_salary

    def update_exp(self, company, new_exp):
        self.companys[company][1] = new_exp

    def show_vacancies(self):
        print(self.name)
        if len(self.companys) != 0:
            for ni in self.companys:
                print(
                    f'"{ni}": зарплата {self.companys[ni][0]} тыс, требуемый опыт {self.companys[ni][1]}')
        else:
            print("Пока нет вакансий на данную профессию")

    def find_best_vacancy(self, exp, profession, min_salary):
        if profession == self.name:
            bcn = None
            for local_comp_name in self.companys:
                ls, le = self.companys[local_comp_name]
                if ls >= min_salary and le <= exp:
                    if bcn is None or (ls >= self.companys[bcn][0] and le <= self.companys[bcn][1]):
                        bcn = local_comp_name
            if bcn is None:
                print("Простите, для вас не нашлось вакансий.")
            else:
                print(
                    f'Наилучшая вакансия для вас в компании "{bcn}" с зарплатой {self.companys[bcn][0]} тыс.')
                self.companys.pop(bcn)
        else:

            print(
                f"Кажется, вы ищете вакансии {profession} в разделе {self.name}. Выберите другой раздел.")
