
```  
public interface EmployeeMapper {

    @Select({"SELECT * FROM employee WHERE id = #{id}", 
              "<if test='aa!=null'>"
              "and aa=#{aa}"
              "</if>"
    })
    @ResultMap("employeeResultMap")
    Employee findById(long id);

}
```  



