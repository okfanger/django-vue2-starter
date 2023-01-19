import datetime
import logging
import os.path

from django.utils import timezone
from tqdm import tqdm
from django.core.management.base import BaseCommand
import pandas as pd
import os
from apps.core.entity.classroom import ClassRoom
from apps.core.entity.course import Course
from apps.core.entity.exam import Exam
from apps.core.entity.question import Question
from apps.core.entity.questionoption import QuestionOption
from apps.core.entity.student import Student
from apps.core.entity.teacher import Teacher
from apps.users import models
from apps.users.models import User

from back.settings import BASE_DIR

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    项目初始化命令: python manage.py init [xxx]
    """

    def add_arguments(self, parser):
        parser.add_argument('init_name', nargs='*', type=str, )

    def handle(self, *args, **options):
        init_name_list: List[str] = options['init_name']
        # 这里可以获取init xxx的内容
