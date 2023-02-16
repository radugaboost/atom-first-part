def squart(a):
    return a ** 2

def create_handlers(callback):
    for step in range(5):
      # добавляем обработчики для каждого шага (от 0 до 4)
      yield lambda: callback(step)

def execute_handlers(handlers):
  # запускаем добавленные обработчики (шаги от 0 до 4)
  for handler in handlers:
    handler()
