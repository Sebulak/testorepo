import platform

def main():
    print("Device Information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    test()
    print(f"Processor: {platform.processor()}")
    

def test():
    print("Running tests...")
    assert platform.system() in ["Windows", "Linux", "Darwin"], "Unsupported OS"
    print("All tests passed!")

if __name__ == "__main__":
    main()