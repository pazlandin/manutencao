from django.db import models

# Create your models here.

class Escada(models.Model):
    codigo = models.CharField(max_length=20)
    data_envio = models.DateField()
    problema = models.CharField(max_length=100)
    
    STATUS_CHOICE = [
        ('pendente', 'Pendente'),
        ('em_manutencao', 'Em manutenção'),
        ('concluida', 'Concluída'),
    ]

    MODELO_CHOICE = [
        ('escada_es-ca_fort_tesoura_pequena', 'ESCADA ES-CA FORT TESOURA PEQUENA'),
        ('escada_es-ca_fort_6m_extensiva', 'ESCADA ES-CA FORT 6M EXTENSIVA'),
    ]

    modelo = models.CharField(max_length=40, choices=MODELO_CHOICE, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pendente')

    def __str__(self):
        return self.codigo