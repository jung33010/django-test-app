# 기반 이미지 설정
FROM python:3.12

# 작업 디에렉토리
WORKDIR /app

# 의존성 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 장고가 노출될 포트
EXPOSE 8000

# 컨테이너 시작할 때 실행될 명령어
# 이건 거의 개발용(dev).
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 이게 운영용

# collectstatic 를 넣으면 build 단계부터 안됨...
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "vogue_me.wsgi:application", "--bind", "0.0.0.0:8000"]