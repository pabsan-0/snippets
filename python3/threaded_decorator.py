def threaded(func):
    """Decorator to run class methods on a different thread"""
    import threading

    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args)
        thread.start()
        return thread

    return wrapper
