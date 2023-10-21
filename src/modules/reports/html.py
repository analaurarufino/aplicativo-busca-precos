from modules.reports.reports import ReportTemplate

class HTMLReport(ReportTemplate):

    def format_report(self, statistics):
        html_report = """
        <html>
        <head>
            <title>Relatorio de Estatisticas do Sistema</title>
        </head>
        <body>
            <h1>Estatisticas do Sistema</h1>
            <h2>Menus Mais Acessados</h2>
            <ul>
        """

        for menu, count in statistics.items():
            html_report += f"<li>{menu}: {count} vezes</li>"

        html_report += """
            </ul>
        </body>
        </html>
        """
        return html_report
    
    def save_report(self, report):
        with open('system_stats.html', 'w') as html_file:
            html_file.write(report)
        print("\nRelatório HTML gerado em 'system_stats.html'")



