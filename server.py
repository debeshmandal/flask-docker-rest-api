#!/usr/bin/env python
"""server.py - auto-generated by softnanotools"""
from flask import Flask, jsonify

from softnanotools.logger import Logger
logger = Logger('SERVER')

app = Flask(__name__)

EXAMPLE = [
    {'a': [1, 2, 3], 'b': [4, 5, 6]},
    {'a': [0, 1, 2], 'b': [5, 8, 8]},
]

@app.route('/example', methods=['GET'])
def get_example():
    return jsonify({'data': EXAMPLE})

def main(**kwargs):
    logger.info('Running server...')
    app.run(debug=True, host="0.0.0.0", port=5000)
    logger.info('Done!')
    return

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='server.py - auto-generated by softnanotools')
    main(**vars(parser.parse_args()))
