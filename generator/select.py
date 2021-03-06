#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andres F. Cardenas
# Email: akardenasjimenez@gmail.com
instructions = (
    'SELECT',
    'WHERE',
    'FROM',
)

def select(table_name, columns=None, table_esp=None, sign='=', value=None):
    """This function represent the select instruction.
    """
    if isinstance(columns, type(None)) is True:
        return '{0} * {1} {2}'.format(
            instructions[0],
            instructions[2],
            table_name
        )

    if isinstance(columns, list) is False:
        return 'ERROR: Data structure invalid, only list type.'

    try:
        columns = ', '.join(columns)
    except TypeError as te:
        return 'ERROR: Column name should be str type: {0}'.format(te)

    # table_esp dependa on value vice versa
    if table_esp != None and value != None:
        return '{0} {1} {2} {3} {4} {5}{6}{7}'.format(
            instructions[0],
            columns,
            instructions[2],
            table_name,
            instructions[1],
            table_esp,
            sign,
            value,
        )

    return '{0} {1} {2} {3}'.format(
        instructions[0],
        columns,
        instructions[2],
        table_name
    )
