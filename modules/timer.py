import schedule
import time
import subprocess

class timer:
    def run_main_script():
        try:
            subprocess.run(["python", "./controller.py"])
        except Exception as e:
            print(f"An error occurred while running main.py: {str(e)}")

    if __name__ == "__main__":
        schedule.every(2).hours.do(run_main_script)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
