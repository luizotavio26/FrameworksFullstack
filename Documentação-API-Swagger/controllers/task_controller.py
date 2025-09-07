from flask import request, jsonify
from models.task import db, Task
from models.user import User


class TaskController:

    @staticmethod
    def list_tasks():
        """
        Listar todas as tarefas
        Este endpoint retorna uma lista de todas as tarefas cadastradas.
        ---
        tags:
          - Tasks
        responses:
          200:
            description: Uma lista de tarefas.
            schema:
              id: Task
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  title:
                    type: string
                  description:
                    type: string
                  status:
                    type: string
                  user_id:
                    type: integer

        """

        tasks = Task.query.all()
        return jsonify(tasks), 200

    @staticmethod
    def create_task():
        """
        Criar uma nova tarefa
        Cria uma nova tarefa com base nos dados fornecidos.
        ---
        tags:
          - Tasks
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - title
                - user_id
              properties:
                title:
                  type: string
                  description: Título da tarefa.
                description:
                  type: string
                  description: Descrição da tarefa.
                user_id:
                  type: integer
                  description: ID do usuário ao qual a tarefa pertence.
        responses:
          201:
            description: Tarefa criada com sucesso.
        """

        title = request.form['title']
        description = request.form['description']
        user_id = request.form['user_id']

        if title and user_id: 
            new_task = Task(
                title=title,
                description=description,
                user_id=user_id
            )
            db.session.add(new_task)
            db.session.commit()

        return jsonify({"message": "Task criada com sucesso"}), 201

    @staticmethod
    def update_task_status(task_id):
        """
        Atualizar uma tarefa
        Atualiza o status de uma tarefa existente.
        ---
        tags:
          - Tasks
        parameters:
          - name: task_id
            in: path
            type: integer
            required: true
            description: O ID da tarefa a ser atualizada.
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - status
              properties:
                status:
                  type: string
                  enum: [Pendente, Concluído]
                  description: Novo status da tarefa.
        responses:
          200:
            description: Tarefa atualizada com sucesso.
          404:
            description: Tarefa não encontrada.   
        """


        task = Task.query.get(task_id)
        if task:
            task.status = "Concluído" if task.status == "Pendente" else "Pendente"
            db.session.commit()
            return jsonify({"message":"Task atualizada com sucesso"}), 200
        return jsonify({"message":"Task não encontrada"}), 404

    @staticmethod
    def delete_task(task_id):
        """
        Excluir uma tarefa
        Remove uma tarefa existente com base no ID.
        ---
        tags:
          - Tasks
        parameters:
          - name: task_id
            in: path
            type: integer
            required: true
            description: O ID da tarefa a ser excluída.
        responses:
          200:
            description: Tarefa excluída com sucesso.
          404:
            description: Tarefa não encontrada.  
        """

        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return jsonify({"message":"Task deletada com sucesso"}), 200
        return jsonify({"message":"Task não encontrada"}), 404
