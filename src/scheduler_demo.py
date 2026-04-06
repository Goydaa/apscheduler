# -*- coding: utf-8 -*-
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def task_1():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Задача 1: Одноразовая задача выполнена!")

def task_2():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Задача 2: Интервальная задача (каждые 3 секунды)")

def task_3():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Задача 3: Задача по расписанию (каждую минуту)")

def task_4():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Задача 4: Задача с параметрами - привет, мир!")

print("=" * 60)
print("APSCHEDULER - ДЕМОНСТРАЦИЯ ПЛАНИРОВАНИЯ ЗАДАЧ")
print("=" * 60)

scheduler = BackgroundScheduler()

print("\n1. ЗАДАЧА С ЗАДЕРЖКОЙ (через 5 секунд)")
print("-" * 40)
run_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
scheduler.add_job(task_1, 'date', run_date=run_time, id='job_date')
print(f"Задача запланирована на {run_time.strftime('%H:%M:%S')}")

print("\n2. ИНТЕРВАЛЬНАЯ ЗАДАЧА (каждые 3 секунды)")
print("-" * 40)
scheduler.add_job(task_2, 'interval', seconds=3, id='job_interval')
print("Задача будет выполняться каждые 3 секунды")

print("\n3. ЗАДАЧА ПО РАСПИСАНИЮ (каждую минуту)")
print("-" * 40)
scheduler.add_job(task_3, 'cron', minute='*', id='job_cron')
print("Задача будет выполняться каждую минуту")

print("\n4. ЗАДАЧА С ПАРАМЕТРАМИ (через 10 секунд)")
print("-" * 40)
scheduler.add_job(task_4, 'date', run_date=datetime.datetime.now() + datetime.timedelta(seconds=10), id='job_args')
print("Задача с параметрами запланирована через 10 секунд")

scheduler.start()
print("\n" + "=" * 60)
print("Планировщик запущен. Нажмите Ctrl+C для остановки.")
print("=" * 60)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nОстановка планировщика...")
    scheduler.shutdown()
    print("Планировщик остановлен. До свидания!")
