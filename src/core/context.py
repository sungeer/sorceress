from contextvars import ContextVar

exec_id_var = ContextVar('exec_id', default='-')
