from flask import request, jsonify
from models.user import User, db

class UserController:
    @staticmethod
    def list_users():
        """
        Listar todos os usuários
        Este endpoint retorna uma lista de todos os usuários cadastrados.
        ---
        tags: 
          - Users
        responses:
          200:
            description: Uma lista de usuários.
            schema:
              id: User
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  email:
                    type: string
        """
        users = User.query.all()
        result = []
        for user in users:
            result.append({
                'id': user.id,
                'name': user.name,
                'email': user.email
            })
        return jsonify(result), 200

    @staticmethod
    def create_user():
        """
        Formulário de contato
        Este endpoint exibe um formulário de contato e processa os dados enviados.
        ---
        tags: 
          - Users
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - name
                - email
              properties:
                name:
                  type: string
                email:
                  type: string
        responses:
          201: 
            description: Usuário criado com sucesso.
          404:
            description: Usuário não encontrado.
        """
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')


        if name and email: 
            new_user = User(
                name=name, 
                email=email
            )
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'Usuário criado com sucesso'}), 201
        return jsonify({'message': 'Usuário não encontrado'}), 404