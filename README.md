# HeyApp
Приложение написанное на фреймворке Django, предназначено для мониторинга узлов ТСКП и
востановления их конфигураций в случае неисправности.
Для монитринга используется платформа Zabbix(из коробки) и движок GoFlow для сбора информации о трафике по протаколу  NetFlow
написанный на языке Go.
Система востановления и графический интерфейс реализованы в качестве Web приложения с использованием языка Python.
