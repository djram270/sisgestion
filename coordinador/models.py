from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(db_column='ASIG_NOMBRE', max_length=100)
    creditos = models.IntegerField(db_column='ASIG_CREDITOS')
    objetivos = models.TextField(db_column='ASIG_OBJETIVOS')
    semestre = models.IntegerField(db_column='ASIG_SEMESTRE')

    ASIG_ID = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'TBL_ASIGNATURA'



class Competencia(models.Model):
    descripcion = models.CharField(db_column='COMP_DESCRIPCION', max_length=250)
    tipo = models.CharField(db_column='COMP_TIPO', max_length=50)
    nivel = models.CharField(db_column='COMP_NIVEL', max_length=50)

    COMP_ID = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'TBL_COMPETENCIA'



class ResultadoAprendizaje(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, db_column='COMP_ID')
    descripcion = models.CharField(db_column='RAP_DESCRIPCION', max_length=250)

    RAP_ID = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'TBL_RA'



class Docente(models.Model):
    tipo_identificacion = models.CharField(db_column='DOC_TIPOIDENTIFICACION', max_length=50)
    tipo_docente = models.CharField(db_column='DOC_TIPODOCENTE', max_length=50)
    nombres = models.CharField(db_column='DOC_NOMBRES', max_length=100)
    apellidos = models.CharField(db_column='DOC_APELLIDOS', max_length=100)
    identificacion = models.CharField(db_column='DOC_IDENTIFICACION', max_length=100)
    titulo = models.CharField(db_column='DOC_TITULO', max_length=100)

    DOC_ID = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'TBL_DOCENTE'


