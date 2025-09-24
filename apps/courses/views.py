from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Principiante',
            'rating': 4.8,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Alisson Walsh',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/42.jpg',
        },
        {
            'id': 2,
            'level': 'Principiante',
            'rating': 5,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Patty Kutch',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg',
        },
        {
            'id': 3,
            'level': 'Principiante',
            'rating': 5,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Alisson Walsh',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
            'id': 4,
            'level': 'Principiante',
            'rating': 5,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Alisson Walsh',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg',
        },
        {
            'id': 5,
            'level': 'Principiante',
            'rating': 5,
            'course_title': 'Python: fundamentos hasta los detalles',
            'instructor': 'Alisson Walsh',
            'course_image': 'images/curso_5.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/45.jpg',
        },
    ]
    return render(request, "courses/courses.html",{
        'courses' : courses
    })

def course_detail(request):
    course = {
        'course_title': 'Django Aplicaciones',
        'course_link': 'course_lessons',
        'course_image': 'images/curso_2.jpg',
        'info_course': {
            'lessons': 79,
            'duration': 8,
            'instructor': 'Ricardo Cuellar'
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Inroduccion al curso',
                'lessons': [
                    {
                        'name': 'Que aprenderas en este curso',
                        'type': 'video',
                    },
                    {
                        'name': 'Como usar la plataforma',
                        'type': 'article',
                    },
                ]
            }
        ]
    }
    return render(request, "courses/course_detail.html",{
        'course':course
        
    })

def course_lessons(request):
    lesson = {
        'course_title': 'Django Aplicaciones',
        'progress': 30,
        'course_content': [
            {
                'id': 1,
                'name': 'Introduccion al curso',
                'total_lessons': 6,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': 'Que aprenderas en este curso',
                        'type': 'video',
                    },
                    {
                        'name': 'Como usar la plataforma',
                        'type': 'article',
                    },
                ]
            },
            {
                'id': 2,
                'name': 'Django principios',
                'total_lessons': 8,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': 'Que aprenderas en este curso',
                        'type': 'video',
                    },
                    {
                        'name': 'Como usar la plataforma',
                        'type': 'article',
                    },
                ]
            },
            {
                'id': 3,
                'name': 'Introduccion al curso',
                'total_lessons': 6,
                'complete_lessons': 3,
                'lessons': [
                    {
                        'name': 'Que aprenderas en este curso',
                        'type': 'video',
                    },
                    {
                        'name': 'Como usar la plataforma',
                        'type': 'article',
                    },
                ]
            }
        ]
    }
    return render(request, 'courses/course_lessons.html',{
        'lesson':lesson
    })