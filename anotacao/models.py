from django.db import models

class TurmaCadetes(models.Model):
    turma = models.CharField(max_length=20, unique=True)
    
    def __str__(self) -> str:
        return self.turma

class UserMilitar(models.Model):
    TIPOS_CARGO = [
        ("Oficial_comandante", "Oficial Comandante"),
        ("Oficial", "Oficial"),
        ("Cadete", "Cadete"),
    ]
    
    nome = models.CharField(max_length=50)
    numerica = models.CharField(max_length=20, null=True, blank=True)
    cargo = models.CharField(max_length=20, choices=TIPOS_CARGO)
    turma = models.ForeignKey(TurmaCadetes, null=True, blank=True, on_delete=models.SET_NULL)
    permissao_anotar = models.BooleanField(default=False)
    senha = models.CharField(max_length=255)
    cadete_de_dia = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.nome} ({self.numerica})"
    
class Anotacao(models.Model):
    TIPOS_ANOTACAO = [
        ("positiva", "Positiva"),
        ("negativa", "Negativa"),
    ]
    TIPOS_DESPACHO = [
        ("pernoite", "Pernoite"),
        ("revista", "Revista"),
        ("outros", "Outros")
    ]
    tipo_anotacao = models.CharField(max_length=10, choices=TIPOS_ANOTACAO)
    motivo = models.TextField()
    cadete_anotado = models.ForeignKey(UserMilitar, on_delete=models.CASCADE) 
    criado_por = models.ForeignKey(UserMilitar, on_delete=models.SET_NULL, null=True, related_name='criado_por')
    status = models.CharField(max_length=20, default='notificada')
    criada_em = models.DateTimeField(auto_now_add=True) 
    despacho = models.CharField(max_length=10, choices=TIPOS_DESPACHO, null=True, blank=True)
    despachado_por = models.ForeignKey(UserMilitar, on_delete=models.SET_NULL, null=True, blank=True, related_name='despachado_por')
    data_cumprimento = models.DateField(null=True, blank=True)

class ArquivoExportado(models.Model):
    nome_arquivo = models.CharField(max_length=255)
    data_exportacao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='exportacoes/')
    exportado_por = models.ForeignKey(UserMilitar, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_arquivo