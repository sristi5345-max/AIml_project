import csv
from collections import defaultdict

GRADE_POINTS = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0,
    "D": 1.0, "F": 0.0,
}

def numeric_to_letter(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

class Course:
    def __init__(self, name, credits, grade, semester):
        self.name = name
        self.credits = credits
        self.grade = grade
        self.semester = semester
        self.grade_points = GRADE_POINTS.get(grade, 0.0)
        self.quality_points = self.credits * self.grade_points

    def to_dict(self):
        return vars(self)

class GPACalculator:
    def __init__(self):
        self.courses = []

    def add_course(self, name, credits, grade, semester):
        try:
            grade = numeric_to_letter(float(grade))
        except:
            grade = grade.upper()

        self.courses.append(Course(name, credits, grade, semester))

    @property
    def cumulative_gpa(self):
        total_q = sum(c.quality_points for c in self.courses)
        total_c = sum(c.credits for c in self.courses)
        return round(total_q / total_c, 3) if total_c else 0

    def semester_gpa(self, sem):
        cs = [c for c in self.courses if c.semester == sem]
        tq = sum(c.quality_points for c in cs)
        tc = sum(c.credits for c in cs)
        return round(tq / tc, 3) if tc else 0

    def gpa_by_semester(self):
        return {s: self.semester_gpa(s) for s in set(c.semester for c in self.courses)}

    def courses_by_semester(self):
        d = defaultdict(list)
        for c in self.courses:
            d[c.semester].append(c)
        return d

    def total_credits(self):
        return sum(c.credits for c in self.courses)

    def grade_distribution(self):
        d = defaultdict(int)
        for c in self.courses:
            d[c.grade] += 1
        return d

    def gpa_trend(self):
        return list(self.gpa_by_semester().items())

    def export_csv(self, path):
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.courses[0].to_dict().keys())
            writer.writeheader()
            for c in self.courses:
                writer.writerow(c.to_dict())
        return path

    def what_if_gpa(self, hyp):
        tc = self.total_credits()
        tq = sum(c.quality_points for c in self.courses)
        for _, cr, gr in hyp:
            tq += cr * GRADE_POINTS.get(gr, 0)
            tc += cr
        return round(tq / tc, 3)