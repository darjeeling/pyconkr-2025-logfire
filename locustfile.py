from locust import HttpUser, task, between

# 반복 횟수 설정 (원하는 값으로 변경 가능)
REQUEST_REPEAT = 20

class MyUser(HttpUser):
    wait_time = between(1, 2)  # 각 요청 사이 대기 시간(초)

    def on_start(self):
        self.counter = 0

    @task
    def call_endpoints(self):
        # /error/ 와 /sleep/ 번갈아 호출
        if self.counter % 2 == 0:
            self.client.get("/error/")
        else:
            self.client.get("/sleep/")

        # REQUEST_REPEAT번 호출마다 /api/ 호출
        if (self.counter + 1) % REQUEST_REPEAT == 0:
            self.client.get("/api/")

        self.counter += 1
