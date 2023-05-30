from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Ordenar os cursos pelo último dia de término
        courses.sort(key=lambda x: x[1])
        # Inicializar a lista de cursos selecionados
        selected_courses = []
        # Inicializar o tempo atual
        current_time = 0
        # Percorrer os cursos
        for duration, lastDay in courses:
            # Verificar se é possível adicionar o curso sem ultrapassar o último dia
            if current_time + duration <= lastDay:
                # Adicionar o curso à lista de cursos selecionados
                selected_courses.append(duration)
                # Atualizar o tempo atual
                current_time += duration
            else:
                # Verificar se é possível substituir um curso com duração maior pelo curso atual
                max_duration_index = -1
                max_duration = 0
                for i, course_duration in enumerate(selected_courses):
                    if course_duration > max_duration:
                        max_duration = course_duration
                        max_duration_index = i
                if max_duration_index != -1 and duration < max_duration:
                    # Substituir o curso com duração maior pelo curso atual
                    selected_courses[max_duration_index] = duration
                    # Atualizar o tempo atual
                    current_time += duration - max_duration
        return len(selected_courses)