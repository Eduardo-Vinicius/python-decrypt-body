import argparse
from app.lambda_function import lambda_handler

handlers = {
    'crypto': lambda_handler
}

strategies_list = [(strategy) for strategy in list(handlers.keys())]
parser = argparse.ArgumentParser()
parser.add_argument('--app',
                    choices=strategies_list,
                    required=True)
if __name__ == '__main__':
    args = parser.parse_args()
    handler = handlers[args.app]
    handler(None, None)